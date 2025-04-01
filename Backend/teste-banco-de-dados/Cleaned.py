import pandas as pd


df = pd.read_csv('1T2024.csv', sep=';', encoding='utf-8', quotechar='"')


df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].replace(',', '.', regex=True).astype(float)
df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].replace(',', '.', regex=True).astype(float)



df.to_csv(
    '1T2024_cleaned.csv',
    sep=';',
    index=False,
    encoding='utf-8',
    quotechar='"',
    quoting=2  
)

print("Arquivo CSV criado com aspas apenas nos campos de texto!")
