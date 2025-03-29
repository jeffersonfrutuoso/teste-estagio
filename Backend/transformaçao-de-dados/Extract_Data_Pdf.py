import pdfplumber
import pandas as pd


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


def processar_pdf(pdf_paths):
    for pdf_path in pdf_paths:
        print(f"Processando o arquivo {pdf_path}...")
        dados_extraidos = extrair_tabela(pdf_path)

        if dados_extraidos:
            nome_csv = f"dados_extraidos_{pdf_path.split('.')[0]}.csv"
            salvar_em_csv(dados_extraidos, nome_csv)
        else:
            print(f"Nenhuma tabela encontrada no PDF {pdf_path}")


pdf_paths = ["Anexo_1.pdf", "Anexo_2.pdf"]  


processar_pdf(pdf_paths)
