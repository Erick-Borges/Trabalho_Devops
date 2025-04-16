from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

RASTREAMENTO_API_BASE_URL = os.environ.get('RASTREAMENTO_API_URL', 'http://localhost:5001')

@app.route('/consultar/<string:codigo>', methods=['GET'])
def consultar_rastreamento(codigo):
    try:
        url_rastreamento = f"{RASTREAMENTO_API_BASE_URL}/rastrear/{codigo}"
        response = requests.get(url_rastreamento, timeout=5) 
        response.raise_for_status() 

        dados_rastreamento = response.json()

        return jsonify({
            "consulta_codigo": codigo,
            "informacao_rastreamento": dados_rastreamento,
            "fonte": "rastreamento-api"
        })

    except requests.exceptions.ConnectionError:
        return jsonify({"erro": "Não foi possível conectar à API de rastreamento"}), 503 
    except requests.exceptions.Timeout:
         return jsonify({"erro": "Timeout ao consultar a API de rastreamento"}), 504 
    except requests.exceptions.RequestException as e:
     
        status_code = response.status_code if 'response' in locals() and response else 500
        return jsonify({"erro": f"Erro ao consultar a API de rastreamento: {str(e)}"}), status_code
    except Exception as e:
      
         return jsonify({"erro": f"Erro interno no servidor de logística: {str(e)}"}), 500

if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=5000)