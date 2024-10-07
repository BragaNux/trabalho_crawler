from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os
import tempfile

app = Flask(__name__)

# Função para realizar scraping no Craigslist com BeautifulSoup
def scrape_craigslist(url):
    # Aqui definimos o cabeçalho da requisição HTTP, incluindo o "User-Agent" para evitar bloqueios do site
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Fazemos a requisição GET no site utilizando o URL e o cabeçalho
    response = requests.get(url, headers=headers)

    # Verificamos se o status da resposta foi bem-sucedido (200 = sucesso)
    if response.status_code != 200:
        # Retorna uma lista vazia se houver erro
        return [], [f"Erro ao acessar o site: {response.status_code}"]

    # Fazemos o "parsing" do HTML recebido para conseguir extrair as informações
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []  # Lista para armazenar produtos encontrados
    not_found_items = []  # Lista para armazenar itens que não foram capturados corretamente

    # Seletores ajustados para capturar os produtos e preços no HTML correto
    for item in soup.find_all('li', class_='cl-static-search-result'):
        try:
            # Captura o nome do produto
            name = item.find('div', class_='title').text.strip()

            # Captura o preço do produto
            price_tag = item.find('div', class_='price')
            if price_tag is not None:
                price = float(price_tag.text.strip('$'))  # Converte o preço para float
            else:
                price = 0.0  # Se não houver preço, define como 0

            # Adiciona o produto e o preço na lista de produtos
            products.append((name, price))
        except Exception as e:
            # Captura os erros na extração de itens
            not_found_items.append(f"Erro ao capturar o item: {str(e)}")

    return products, not_found_items

# Função para realizar scraping no site Books to Scrape
def scrape_books(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return [], [f"Erro ao acessar o site: {response.status_code}"]

    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    not_found_items = []

    # Encontrar os produtos na página
    for item in soup.find_all('article', class_='product_pod'):
        try:
            # Captura o nome e o preço de cada produto
            name = item.find('h3').find('a')['title']
            price = float(item.find('p', class_='price_color').text.strip('£'))
            products.append((name, price))
        except Exception as e:
            not_found_items.append(f"Erro ao capturar o item: {str(e)}")

    return products, not_found_items

# Função que implementa o algoritmo Bubble Sort para ordenar os produtos
def bubble_sort(products):
    n = len(products)  # Pega o tamanho da lista de produtos
    # Loop para percorrer toda a lista
    for i in range(n):
        # Loop interno para comparar e trocar elementos adjacentes
        for j in range(0, n - i - 1):
            if products[j][1] > products[j + 1][1]:  # Compara os preços
                # Troca os elementos de lugar se estiverem fora de ordem
                products[j], products[j + 1] = products[j + 1], products[j]

# Função de ordenação externa para lidar com grandes volumes de dados
def external_sort(products):
    temp_files = []  # Lista para armazenar arquivos temporários
    
    # Define um tamanho de chunk para processar pequenos blocos de produtos por vez
    chunk_size = 100  # Cada bloco terá no máximo 100 produtos
    for i in range(0, len(products), chunk_size):
        chunk = products[i:i + chunk_size]  # Cria o bloco
        bubble_sort(chunk)  # Ordena o bloco usando o Bubble Sort

        # Salva o bloco ordenado em um arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
        for item in chunk:
            temp_file.write(f"{item[0]},{item[1]}\n")  # Escreve os produtos no arquivo
        temp_files.append(temp_file.name)  # Armazena o nome do arquivo
        temp_file.close()  # Fecha o arquivo para garantir que ele está salvo

    # Mescla todos os blocos ordenados em um arquivo final
    sorted_products = merge_chunks(temp_files)

    # Remove os arquivos temporários após a mesclagem
    for temp_file in temp_files:
        os.remove(temp_file)

    return sorted_products

# Função para mesclar os blocos ordenados em arquivos temporários
def merge_chunks(temp_files):
    sorted_products = []  # Lista final de produtos ordenados

    # Abre todos os arquivos temporários
    files = [open(file, 'r') for file in temp_files]
    current_lines = [file.readline().strip().split(',') for file in files]  # Lê a primeira linha de cada arquivo

    while any(current_lines):  # Continua enquanto houver linhas a serem lidas
        min_index = None
        min_value = float('inf')

        # Encontra o menor valor entre as linhas atuais
        for i, line in enumerate(current_lines):
            if line and float(line[1]) < min_value:
                min_value = float(line[1])
                min_index = i

        # Adiciona o menor valor à lista final e lê a próxima linha do arquivo correspondente
        if min_index is not None:
            sorted_products.append((current_lines[min_index][0], min_value))
            current_lines[min_index] = files[min_index].readline().strip().split(',')

    # Fecha os arquivos temporários
    for file in files:
        file.close()

    return sorted_products

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('site')

    # Verifica se o site escolhido é o Craigslist ou o Books to Scrape
    if 'craigslist' in url:
        products, not_found_items = scrape_craigslist(url)
    elif 'books.toscrape.com' in url:
        products, not_found_items = scrape_books(url)
    else:
        products, not_found_items = [], ["Site não suportado"]

    if not products:  # Caso não haja produtos encontrados, mostra mensagem de erro
        message = "Nenhum produto foi encontrado. Verifique o site ou o código de scraping."
        return render_template('results.html', message=message, products=None, not_found_items=not_found_items)
    
    # Se houver muitos produtos, usa a ordenação externa, senão, usa Bubble Sort
    if len(products) > 1000:  # Define um limite arbitrário de 1000 produtos
        products = external_sort(products)
    else:
        bubble_sort(products)

    return render_template('results.html', products=products, not_found_items=not_found_items)

if __name__ == '__main__':
    app.run(debug=True)
