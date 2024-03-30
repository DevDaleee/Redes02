from flask import Flask, request
import math

app = Flask(__name__)

def calcular_fatorial(n):
    return str(math.factorial(n))

def calcular_arranjo(n, r):
    try:
        return str(math.perm(n, r))
    except ValueError as e:
        return f"Erro ao calcular o arranjo de {n} elementos tomados {r}: {str(e)}"

def calcular_combinacao(n, r):
    try:
        return str(math.comb(n, r))
    except ValueError as e:
        return f"Erro ao calcular a combinação de {n} elementos tomados {r}: {str(e)}"

def calcular_permutacao(n):
    return str(math.perm(n, n))

@app.route('/')
def index():
    return "Servidor de cálculos está em execução!"

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    if 'funcao' not in data:
        return "Erro: 'funcao' não especificada.", 400
    
    if data['funcao'] == 'fatorial':
        if 'numero' not in data:
            return "Erro: 'numero' não especificado para o cálculo do fatorial.", 400
        resultado = calcular_fatorial(data['numero'])
    elif data['funcao'] == 'arranjo':
        if 'n' not in data or 'r' not in data:
            return "Erro: 'n' ou 'r' não especificados para o cálculo do arranjo.", 400
        resultado = calcular_arranjo(data['n'], data['r'])
    elif data['funcao'] == 'combinacao':
        if 'n' not in data or 'r' not in data:
            return "Erro: 'n' ou 'r' não especificados para o cálculo da combinação.", 400
        resultado = calcular_combinacao(data['n'], data['r'])
    elif data['funcao'] == 'permutacao':
        if 'numero' not in data:
            return "Erro: 'numero' não especificado para o cálculo da permutação.", 400
        resultado = calcular_permutacao(data['numero'])
    else:
        return "Erro: Função não reconhecida.", 400
    
    return resultado

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
