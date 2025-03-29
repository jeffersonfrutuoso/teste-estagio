import requests
import pdfplumber
import pandas as pd
import zipfile
import os
from bs4 import BeautifulSoup


def extrair_tabela(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        
        all_pages_text = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                all_pages_text.extend(table)  
        return all_pages_text


def salvar_em_csv(dados, nome_arquivo):
    
    df = pd.DataFrame(dados[1:], columns=dados[0])  
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo CSV salvo como {nome_arquivo}")


def substituir_abreviacoes(df):
    
    df['OD'] = df['OD'].replace({'OD': 'seg. Odontológica'})
    df['AMB'] = df['AMB'].replace({'AMB': ' seg. Ambulatorial'})
    return df

def salvar_em_csv_com_substituicoes(dados, nome_arquivo):
    
    df = pd.DataFrame(dados[1:], columns=dados[0])  

    
    df = substituir_abreviacoes(df)

    
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo CSV com abreviações substituídas salvo como {nome_arquivo}")


def compactar_em_zip(arquivos_csv, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
        for arquivo_csv in arquivos_csv:
            zipf.write(arquivo_csv, os.path.basename(arquivo_csv))  
    print(f"Arquivos compactados em {nome_arquivo_zip}")


def processar_pdf_com_substituicoes(pdf_paths):
    arquivos_csv = []  
    for pdf_path in pdf_paths:
        print(f"Processando o arquivo {pdf_path}...")
        dados_extraidos = extrair_tabela(pdf_path)

        if dados_extraidos:
            nome_csv = f"dados_extraidos_{pdf_path.split('.')[0]}.csv"
            salvar_em_csv_com_substituicoes(dados_extraidos, nome_csv)
            arquivos_csv.append(nome_csv)  
        else:
            print(f"Nenhuma tabela encontrada no PDF {pdf_path}")
    
    return arquivos_csv

def main():
    
    pdf_paths = ["Anexo_1.pdf", "Anexo_2.pdf"]

   
    arquivos_csv = processar_pdf_com_substituicoes(pdf_paths)

    
    compactar_em_zip(arquivos_csv, "Teste_jefferson.zip")

if __name__ == "__main__":
    main()
