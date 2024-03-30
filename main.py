import socket
import math

def calcular_fatorial(n):
    return str(math.factorial(n))

def calcular_arranjo(n, r):
    return str(math.perm(n, r))

def calcular_combinacao(n, r):
    return str(math.comb(n, r))

def calcular_permutacao(n):
    return str(math.perm(n, n))

def main():
    host = ''
    port = 8000

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, port))

    servidor_socket.listen(1)

    while True:
        conexao, endereco = servidor_socket.accept()

        dados = conexao.recv(1024).decode()
        comando, *numeros = dados.split(',')

        numeros = list(map(int, numeros))

        if comando == "fatorial":
            resultado = calcular_fatorial(*numeros)
        elif comando == "arranjo":
            resultado = calcular_arranjo(*numeros)
        elif comando == "combinacao":
            resultado = calcular_combinacao(*numeros)
        elif comando == "permutacao":
            resultado = calcular_permutacao(*numeros)
        else:
            resultado = "Função não reconhecida"

        conexao.send(resultado.encode())
        conexao.close()

if __name__ == "__main__":
    main()
