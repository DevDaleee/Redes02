import socket
import time
import datetime

def main():
    host = '172.20.0.2'
  # Substitua pelo endereço IP do servidor
    port = 3333
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message_count = 0
    print("Sending Messages")
    while message_count < 1000:
        message = f"Message {message_count+1} - Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        client_socket.sendto(message.encode(), (host, port))
        message_count += 1
        time.sleep(0.01)
    
    client_socket.close()

if __name__ == "__main__":
    main()
