import requests
from bs4 import BeautifulSoup

# URL do site da ANS
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Fazer requisição para pegar o HTML da página
response = requests.get(URL)
if response.status_code != 200:
    print("Erro ao acessar o site")
    exit()

# Analisar o HTML com BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Procurar links que levam aos PDFs
pdf_links = []
for link in soup.find_all("a", href=True):
    if "Anexo" in link.text and link["href"].endswith(".pdf"):
        pdf_links.append(link["href"])

# Se não encontrar links, exibir erro
if not pdf_links:
    print("Nenhum PDF encontrado")
    exit()

# Baixar os PDFs encontrados
for idx, pdf_url in enumerate(pdf_links, start=1):
    pdf_url = pdf_url if pdf_url.startswith("http") else "https://www.gov.br" + pdf_url
    pdf_name = f"Anexo_{idx}.pdf"

    response = requests.get(pdf_url)
    with open(pdf_name, "wb") as f:
        f.write(response.content)

    print(f"PDF baixado: {pdf_name}")

print("Download concluído!")
