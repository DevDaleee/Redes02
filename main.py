from flask import Flask, request, jsonify
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

@app.route('/fatorial')
def fatorial():
    numeros = list(map(int, request.args.getlist('numeros')))
    resultado = calcular_fatorial(*numeros)
    return jsonify({'resultado': resultado})

@app.route('/arranjo')
def arranjo():
    numeros = list(map(int, request.args.getlist('numeros')))
    resultado = calcular_arranjo(*numeros)
    return jsonify({'resultado': resultado})

@app.route('/combinacao')
def combinacao():
    numeros = list(map(int, request.args.getlist('numeros')))
    resultado = calcular_combinacao(*numeros)
    return jsonify({'resultado': resultado})

@app.route('/permutacao')
def permutacao():
    numeros = list(map(int, request.args.getlist('numeros')))
    resultado = calcular_permutacao(*numeros)
    return jsonify({'resultado': resultado})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
