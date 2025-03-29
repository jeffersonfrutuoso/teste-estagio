from flask import Flask, request, jsonify
import pandas as pd
import numpy as np  
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


df = pd.read_csv('Relatorio_cadop.csv', encoding='utf-8', sep=';')

@app.route('/api/operadoras', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('q', '').lower()
    
    if not termo:
        return jsonify([])
    
    
    resultados = df[
        df['Razao_Social'].str.lower().str.contains(termo, na=False) |
        df['Nome_Fantasia'].str.lower().str.contains(termo, na=False)
    ].head(20)

    
    resultados = resultados.replace({np.nan: None}).to_dict('records')
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
