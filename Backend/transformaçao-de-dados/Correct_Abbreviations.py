import pandas as pd


csv_file = "dados_extraidos_Anexo_1.csv"


df = pd.read_csv(csv_file)


df.replace({"OD": "Seg. Odontológico", "AMB": "Seg. Ambulatorial"}, inplace=True)


csv_corrigido = "dados_corrigidos.csv"
df.to_csv(csv_corrigido, index=False)

print(f"Arquivo corrigido salvo como {csv_corrigido}")
