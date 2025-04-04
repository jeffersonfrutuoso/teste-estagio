import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT", 3306),
    allow_local_infile=True
)

cursor = conn.cursor(buffered=True)  

print("Conexão bem-sucedida ao MySQL!")


with open(r"C:\Users\jeffe\documents\teste-estagio\Backend\teste-banco-de-dados\scripts.sql", "r", encoding="utf-8") as script_file:
    sql_script = script_file.read()


commands = sql_script.split(";\n")


for command in commands:
    if command.strip():
        try:
            cursor.execute(command)
            print(f"Executado: {command.strip().split('\n')[0]}") 
        except mysql.connector.Error as err:
            print(f"Erro ao executar o comando:\n{command}\nErro: {err}")


conn.commit()
print("Script SQL executado com sucesso!")

cursor.close()
conn.close()
