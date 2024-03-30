import socket
import time
import datetime
import statistics

def main():
    host = '0.0.0.0'
    port = 3333
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    
    print("UDP Server initialized, waiting for connections...")
    
    delays = []
    message_count = 0
    while message_count < 1000:
        start_time = time.time()
        data, address = server_socket.recvfrom(1024)
        end_time = time.time()
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Receiving from {address}: {data.decode()} - Time: {current_time}")
        
        delay = end_time - start_time
        delays.append(delay)
        
        message_count += 1
    
    server_socket.close()
    
    print("Min Delay:", min(delays))
    print("AVG Delay:", statistics.mean(delays))
    print("Max Delay:", max(delays))
    print("Std Delay:", statistics.stdev(delays))

if __name__ == "__main__":
    main()
