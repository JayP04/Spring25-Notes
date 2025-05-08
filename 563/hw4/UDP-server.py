import sys
import socket
from datetime import datetime

# conditioning for correct usage
if len(sys.argv) != 2:
    print("Usage: python UDP-server.py <server-port-number>")
    sys.exit(1)

server_port = int(sys.argv[1])

## since its udp, we wont need welcoming socket. 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", server_port))##using 0.0.0 to seamless connection with any ip
print(f"UDP - listening on port {server_port}.....")

## endless looping
while True:
    ##first get the data and client add
    data, client_add = server_socket.recvfrom(1024)##receiving

    ##for future purposes, im conditioning if the request is request_time
    if data.decode('utf-8') == "REQUEST_TIME":
        now = datetime.utcnow()
        stamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        server_socket.sendto(stamp.encode(), client_add)
        print(f"time stamp sent! to {client_add}")