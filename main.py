from flask import Flask, request
import math

app = Flask(__name__)

def calcular_fatorial(n):
    if n < 0:
        return "Erro: O fatorial não está definido para números negativos."
    resultado = math.factorial(n)
    return f"A fatorial de {n} é {resultado}"

def calcular_arranjo(n, r):
    if n < 0 or r < 0:
        return "Erro: O arranjo não está definido para números negativos."
    try:
        resultado = math.perm(n, r)
        return f"O arranjo de {n} elementos tomados {r} é {resultado}"
    except ValueError as e:
        return f"Erro ao calcular o arranjo de {n} elementos tomados {r}: {str(e)}"

def calcular_combinacao(n, r):
    if n < 0 or r < 0:
        return "Erro: A combinação não está definida para números negativos."
    try:
        resultado = math.comb(n, r)
        return f"A combinação de {n} elementos tomados {r} é {resultado}"
    except ValueError as e:
        return f"Erro ao calcular a combinação de {n} elementos tomados {r}: {str(e)}"

def calcular_permutacao(n):
    if n < 0:
        return "Erro: A permutação não está definida para números negativos."
    resultado = math.perm(n, n)
    return f"A permutação de {n} elementos é {resultado}"

@app.route('/')
def index():
    return "Servidor de cálculos está em execução!"

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    if not data:
        return "Erro: Nenhum dado foi enviado.", 400

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
