import socket
import math

def calcular_fatorial(n):
    return math.factorial(n)

def calcular_arranjo(n, r):
    return math.perm(n, r)

def calcular_combinacao(n, r):
    return math.comb(n, r)

def calcular_permutacao(n):
    return math.perm(n, n)

def main():
    host = ''
    port = 12345

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, port))

    servidor_socket.listen(1)

    while True:
        conexao, endereco = servidor_socket.accept()

        dados = conexao.recv(1024).decode()

        if dados == "fatorial":
            resultado = str(calcular_fatorial(5))
        elif dados == "arranjo":
            resultado = str(calcular_arranjo(5, 2))
        elif dados == "combinacao":
            resultado = str(calcular_combinacao(5, 2))
        elif dados == "permutacao":
            resultado = str(calcular_permutacao(5))
        else:
            resultado = "Função não reconhecida"

        conexao.send(resultado.encode())
        conexao.close()

if __name__ == "__main__":
    main()
