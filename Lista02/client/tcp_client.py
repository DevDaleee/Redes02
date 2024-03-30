import socket
import time

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.21.0.2', 8080))
    
    for i in range(1000):
        sent_time = time.time()
        client_socket.send((str(sent_time) + ',').encode())
    
    client_socket.close()

if __name__ == "__main__":
    client()
