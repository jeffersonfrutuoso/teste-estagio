import requests
import pdfplumber
import pandas as pd
import zipfile
import os
from bs4 import BeautifulSoup

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

# Função para substituir abreviações
def substituir_abreviacoes(df):
    # Substituindo as abreviações pelas descrições completas
    df['OD'] = df['OD'].replace({'OD': 'Outros Despesas'})
    df['AMB'] = df['AMB'].replace({'AMB': 'Ambulatorial'})
    return df

# Função para salvar o CSV com as substituições
def salvar_em_csv_com_substituicoes(dados, nome_arquivo):
    # Convertendo os dados para um DataFrame do pandas
    df = pd.DataFrame(dados[1:], columns=dados[0])  # Dados[0] são os cabeçalhos

    # Substituindo as abreviações
    df = substituir_abreviacoes(df)

    # Salvando o novo CSV
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo CSV com abreviações substituídas salvo como {nome_arquivo}")

# Função para compactar os arquivos CSV em um ZIP
def compactar_em_zip(arquivos_csv, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
        for arquivo_csv in arquivos_csv:
            zipf.write(arquivo_csv, os.path.basename(arquivo_csv))  # Adiciona o arquivo CSV no ZIP
    print(f"Arquivos compactados em {nome_arquivo_zip}")

# Função para processar os arquivos PDF e gerar os CSVs
def processar_pdf_com_substituicoes(pdf_paths):
    arquivos_csv = []  # Lista para armazenar os arquivos CSV gerados
    for pdf_path in pdf_paths:
        print(f"Processando o arquivo {pdf_path}...")
        dados_extraidos = extrair_tabela(pdf_path)

        if dados_extraidos:
            nome_csv = f"dados_extraidos_{pdf_path.split('.')[0]}.csv"
            salvar_em_csv_com_substituicoes(dados_extraidos, nome_csv)
            arquivos_csv.append(nome_csv)  # Adicionando o novo CSV à lista de arquivos CSV
        else:
            print(f"Nenhuma tabela encontrada no PDF {pdf_path}")
    
    return arquivos_csv

# Função principal para baixar, processar e compactar tudo
def main():
    # Caminhos dos PDFs (Anexo 1 e Anexo 2)
    pdf_paths = ["Anexo_1.pdf", "Anexo_2.pdf"]

    # Processar os PDFs e gerar os arquivos CSV
    arquivos_csv = processar_pdf_com_substituicoes(pdf_paths)

    # Compactar os arquivos CSV em um arquivo ZIP
    compactar_em_zip(arquivos_csv, "Teste_jefferson.zip")

if __name__ == "__main__":
    main()
