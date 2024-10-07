# 🖥️ CPD - Trabalho Prático 1 - Crawler de Busca

Este repositório contém um projeto prático desenvolvido como parte da disciplina de CPD. O objetivo do trabalho é criar um **crawler** 📡 para buscar dados de um site de e-commerce e ordenar os produtos coletados por **ordem crescente de preço** 💸. A implementação inclui a utilização BubbleSort de ordenação estudado ao longo da cadeira e uma versão pra trabalhar com externo.

## 📌 Descrição do Projeto

O projeto é dividido em três partes principais:

1. **Coleta de Dados** 📊: Utilização de um crawler para extrair informações dos produtos.
2. **Ordenação dos Produtos** 🔄: Aplicação de um algoritmo de ordenação para ordenar a lista de produtos em ordem crescente de preço.
3. **Ordenação Externa (Opcional)** 💾: Implementação de um algoritmo de ordenação externa para grandes volumes de dados que não cabem na memória.

## 🛠️ Tecnologias Utilizadas

- **Linguagem de Programação**: Python & HTML
- **Bibliotecas**:
  - **Requests**: Para realizar requisições HTTP e obter o HTML das páginas.
  - **BeautifulSoup**: Para fazer o parsing do HTML e extrair os dados necessários.
  - **Flask**: Para criar uma interface web e permitir a interação com o script.

## 📂 Estrutura do Repositório

- **📄 app.py**: Script contendo a aplicação Flask para criar uma interface web para o projeto.
- **📑 README.md**: Documentação do projeto, incluindo instruções de uso e descrição dos objetivos.
- **📦 requirements.txt**: Lista de dependências para instalar as bibliotecas necessárias.
- **📂 templates**:
  - **📄 index.html**: Página inicial para iniciar o scraping.
  - **📄 results.html**: Página de resultados para exibir os produtos ordenados.

## 🚀 Execução do Projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório**:
   
sh
   git clone <link_do_repositorio>

2. **Instale as dependências**:
   
sh
   pip install -r requirements.txt

3. **Execute a aplicação Flask**:
   
sh
   python app.py


## 👥 Colaboradores

- **👤 Brayan Martins**
- **👤 Carlos Daniel Martins**

## 📢 Observação

Duração de 5 a 10 minutos, abordando as seguintes etapas: site utilizado, algoritmo de ordenação escolhido, justificativa das escolhas e resultados obtidos.

## 📝 Organização

- **Notion**: [Link para a organização do projeto](https://www.notion.so/CPD-TRABALHO-cb9ead442bc34965897eefdf3d5bee80?pvs=4)

## 💡 Interface do Usuário

- **Página Inicial**: O usuário pode escolher de qual site deseja buscar os produtos (laptops, tablets, telefones).
- **Resultados**: Exibe os produtos encontrados, seus preços e, em uma seção separada, informações sobre itens que não foram capturados corretamente ou que apresentaram erros.

## 🔗 Sites utilizados

- [Books to Scrape](http://books.toscrape.com)
- [Craigslist](https://bn.craigslist.org/search/ata#search=1~gallery~0~0)

## 📄 Documentos Utilizados

- [Documentação do BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
- [Documentação do Requests](https://requests.readthedocs.io/en/latest/)
- [Documentação do Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Ordenação Externa](https://www.geeksforgeeks.org/external-sorting/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

## 🎥 Video

- [CPD - TRABALHO CRAWLER](https://youtu.be/I2O1biixYlI)
