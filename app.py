from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lista para armazenar os produtos e produtos não encontrados
    products = []
    not_found_items = []

    # Extrair produtos
    for item in soup.find_all('article', class_='product_pod'):
        name_tag = item.find('h3').find('a')
        price_tag = item.find('p', class_='price_color')

        # Verificação
        if name_tag is not None and price_tag is not None:
            name = name_tag['title']  # O título do livro está no atributo 'title'
            try:
                price = float(price_tag.text.strip('£'))  # O preço está com o símbolo '£'
                products.append((name, price))
            except ValueError:
                not_found_items.append(f"Erro ao converter o preço do produto: {name}")
        else:
            not_found_items.append(f"Elemento não encontrado para item: {item.prettify()}")

    print(f"Produtos Capturados: {products}")  # Print Depuração
    print(f"Itens não encontrados: {not_found_items}")  # Print Depuração

    return products, not_found_items

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j][1] > products[j + 1][1]:
                products[j], products[j + 1] = products[j + 1], products[j]

def get_sorted_products(url):
    # Scraping dos produtos
    products, not_found_items = scrape_site(url)
    
    # Ordenando os produtos usando Bubble Sort
    bubble_sort(products)
    
    return products, not_found_items

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('site')
    products, not_found_items = get_sorted_products(url)
    if not products:
        message = "Nenhum produto foi encontrado. Verifique o site ou o código de scraping."
        print("Nenhum produto encontrado.")  # Print para depuração
        return render_template('results.html', message=message, products=None, not_found_items=not_found_items)
    print(f"Produtos a serem exibidos: {products}")  # Print para depuração
    return render_template('results.html', products=products, not_found_items=not_found_items)

if __name__ == '__main__':
    app.run(debug=True)
