import pdfplumber
import pandas as pd

# Função para extrair a tabela do PDF
def extrair_tabela(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Aqui estamos pegando todas as páginas do PDF
        all_pages_text = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                all_pages_text.extend(table)  # Adiciona as tabelas de todas as páginas
        return all_pages_text

# Função para salvar os dados extraídos em um CSV
def salvar_em_csv(dados, nome_arquivo):
    # Convertendo os dados para um DataFrame do pandas
    df = pd.DataFrame(dados[1:], columns=dados[0])  # Dados[0] são os cabeçalhos
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo CSV salvo como {nome_arquivo}")

# Função para processar múltiplos arquivos
def processar_pdf(pdf_paths):
    for pdf_path in pdf_paths:
        print(f"Processando o arquivo {pdf_path}...")
        dados_extraidos = extrair_tabela(pdf_path)

        if dados_extraidos:
            nome_csv = f"dados_extraidos_{pdf_path.split('.')[0]}.csv"
            salvar_em_csv(dados_extraidos, nome_csv)
        else:
            print(f"Nenhuma tabela encontrada no PDF {pdf_path}")

# Lista de arquivos PDF
pdf_paths = ["Anexo_1.pdf", "Anexo_2.pdf"]  # Coloque os nomes corretos dos arquivos

# Processar os arquivos
processar_pdf(pdf_paths)
