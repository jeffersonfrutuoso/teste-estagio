import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('1T2024.csv', sep=';', encoding='utf-8')

# Converter vírgulas em pontos nos valores numéricos
df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

# Salvar um novo CSV corrigido
df.to_csv('1T2024_cleaned.csv', sep=';', index=False, encoding='utf-8')
