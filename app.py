from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Função para scraping no Craigslist com BeautifulSoup
def scrape_craigslist(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)

    # Verificar se a resposta foi bem-sucedida
    if response.status_code != 200:
        return [], [f"Erro ao acessar o site: {response.status_code}"]

    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    not_found_items = []

    # Seletores ajustados para capturar os produtos e preços corretamente
    for item in soup.find_all('li', class_='cl-static-search-result'):
        try:
            # Nome do produto
            name = item.find('div', class_='title').text.strip()

            # Preço do produto
            price_tag = item.find('div', class_='price')
            if price_tag is not None:
                price = float(price_tag.text.strip('$'))
            else:
                price = 0.0  # Caso não haja preço

            products.append((name, price))
        except Exception as e:
            not_found_items.append(f"Erro ao capturar o item: {str(e)}")

    return products, not_found_items

# Função de scraping para o Books to Scrape
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
            name = item.find('h3').find('a')['title']
            price = float(item.find('p', class_='price_color').text.strip('£'))
            products.append((name, price))
        except Exception as e:
            not_found_items.append(f"Erro ao capturar o item: {str(e)}")

    return products, not_found_items

# Função de ordenação com Bubble Sort
def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j][1] > products[j + 1][1]:
                products[j], products[j + 1] = products[j + 1], products[j]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('site')

    if 'craigslist' in url:
        products, not_found_items = scrape_craigslist(url)
    elif 'books.toscrape.com' in url:
        products, not_found_items = scrape_books(url)
    else:
        products, not_found_items = [], ["Site não suportado"]

    if not products:
        message = "Nenhum produto foi encontrado. Verifique o site ou o código de scraping."
        return render_template('results.html', message=message, products=None, not_found_items=not_found_items)
    
    # Ordenar os produtos usando Bubble Sort
    bubble_sort(products)

    return render_template('results.html', products=products, not_found_items=not_found_items)

if __name__ == '__main__':
    app.run(debug=True)
