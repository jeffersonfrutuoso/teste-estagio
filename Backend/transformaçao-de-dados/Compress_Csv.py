import zipfile


csv_file = "dados_extraidos_Anexo_1.csv"


zip_file_name = f"Teste_Jefferson.zip"


with zipfile.ZipFile(zip_file_name, "w") as zipf:
    zipf.write(csv_file)

print(f"Arquivo {zip_file_name} criado com sucesso!")
