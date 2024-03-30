import socket
import time
import statistics

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    
    delays = []
    total_messages = 0
    data = b""
    
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        data += chunk

    sent_times = data.decode().split(',')
    
    for sent_time_str in sent_times:
        sent_time = float(sent_time_str)
        recv_time = time.time()
        delay = recv_time - sent_time
        delays.append(delay)
        total_messages += 1
        if total_messages >= 1000:
            break
    
    conn.close()
    server_socket.close()
    
    return delays

if __name__ == "__main__":
    delays = server()
    print("Minimum delay:", min(delays))
    print("Maximum delay:", max(delays))
    print("Average delay:", statistics.mean(delays))
    print("Standard deviation of delays:", statistics.stdev(delays))
