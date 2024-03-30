import socket

def main():
    host = 'coloque_o_ip_do_back4app_aqui'
    port = 12345

    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, port))

    cliente_socket.send("fatorial".encode())
    resultado_fatorial = cliente_socket.recv(1024).decode()
    print("Resultado do fatorial:", resultado_fatorial)

    cliente_socket.send("arranjo".encode())
    resultado_arranjo = cliente_socket.recv(1024).decode()
    print("Resultado do arranjo:", resultado_arranjo)

    cliente_socket.send("combinacao".encode())
    resultado_combinacao = cliente_socket.recv(1024).decode()
    print("Resultado da combinação:", resultado_combinacao)

    cliente_socket.send("permutacao".encode())
    resultado_permutacao = cliente_socket.recv(1024).decode()
    print("Resultado da permutação:", resultado_permutacao)

    cliente_socket.close()

if __name__ == "__main__":
    main()
