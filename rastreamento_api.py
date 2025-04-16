from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/rastrear/<string:codigo>', methods=['GET'])
def rastrear_pacote(codigo):
    estados_possiveis = [
        "Objeto postado",
        "Objeto em trânsito - por favor aguarde",
        "Objeto saiu para entrega ao destinatário",
        "Objeto entregue ao destinatário",
        "Objeto não localizado no fluxo postal"
    ]

    status_simulado = random.choice(estados_possiveis)
    if "não encontrado" in codigo.lower():
         status_simulado = "Objeto não encontrado"

    return jsonify({
        "codigo_rastreio": codigo,
        "status": status_simulado,
        "data_hora": "2025-04-15T19:30:00Z 
    })

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5001)