🖥️ CPD - Trabalho Prático 1 - Crawler de Busca
Este repositório contém o projeto prático desenvolvido como parte da disciplina de CPD. O objetivo é criar um crawler 📡 que busca dados de um site de e-commerce e ordena os produtos coletados por ordem crescente de preço 💸. A implementação inclui a utilização do algoritmo BubbleSort, estudado ao longo da disciplina.

📌 Descrição do Projeto
O projeto é dividido em três partes principais:

Coleta de Dados 📊: Uso de um crawler para extrair informações dos produtos de e-commerce.
Ordenação dos Produtos 🔄: Aplicação do algoritmo BubbleSort para organizar a lista de produtos em ordem crescente de preço.
Ordenação Externa (Opcional) 💾: Implementação opcional de um algoritmo de ordenação externa para lidar com grandes volumes de dados que não cabem na memória.
🛠️ Tecnologias Utilizadas
Linguagem de Programação: Python
Bibliotecas:
Requests: Realiza requisições HTTP para obter o HTML das páginas.
BeautifulSoup: Faz o parsing do HTML e extrai os dados dos produtos.
Flask: Cria uma interface web para interagir com o script de maneira simples.
📂 Estrutura do Repositório
📄 app.py: Contém a aplicação Flask, que fornece a interface web para o projeto..
📑 README.md: Documentação com instruções de uso e descrição do projeto.
📦 requirements.txt: Lista de dependências do projeto, como as bibliotecas necessárias.
📂 templates:
📄 index.html: Página inicial onde o usuário seleciona o site para buscar os produtos.
📄 results.html: Exibe os produtos encontrados e ordenados, além de itens com erros.
🚀 Como Executar o Projeto
Siga as instruções abaixo para rodar o projeto localmente:

Clone o repositório:
sh
Copiar código
git clone <link_do_repositorio>
Instale as dependências:
sh
Copiar código
pip install -r requirements.txt
Execute a aplicação Flask:
sh
Copiar código
python app.py
Acesse o site local no navegador, normalmente em http://127.0.0.1:5000.

👥 Colaboradores
👤 Daniel: ??
👤 Brayan: ??
📢 Observações
A apresentação deve ter entre 5 e 10 minutos, abordando as seguintes etapas:

Site utilizado: Qual site de e-commerce foi escolhido para o projeto.
Algoritmo de ordenação: Justificativa do uso do BubbleSort.
Resultados obtidos: Principais resultados da ordenação dos produtos.
📊 Apresentação
Canva: Link para a apresentação
📝 Organização do Projeto
Notion: Link para organização do projeto no Notion
💡 Interface do Usuário
Página Inicial: O usuário seleciona o site de e-commerce de onde deseja buscar os produtos (como laptops, tablets ou telefones).
Página de Resultados: Exibe os produtos encontrados, seus preços e, em uma seção separada, os itens que não foram capturados corretamente ou apresentaram erros.
