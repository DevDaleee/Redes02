import socket
import time
import datetime

def main():
    host = '127.0.0.1'
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message_count = 0
    print("Sending Messages")
    while message_count < 1000:
        message = f"Message {message_count+1} - Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        client_socket.sendto(message.encode(), (host, port))
        try:
            client_socket.settimeout(1)
            data, server_address = client_socket.recvfrom(1024)
            print(f"Received confirmation from server: {data.decode()}")
        except socket.timeout:
            print("Timeout occurred. Resending message...")
            continue
        
        message_count += 1
        time.sleep(0.01)
    
    client_socket.close()

if __name__ == "__main__":
    main()
