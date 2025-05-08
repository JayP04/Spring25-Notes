import sys
import socket
from datetime import datetime

##firstly getting the port number from cmd line arg
if len(sys.argv) != 2:
    print("Usage: python TCP-server.py <server-port-number>")
    sys.exit()
server_port = int(sys.argv[1]) ## server port 

## here ill create the welcomeing socket. (code from classs slides)
server_welcome_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_welcome_socket.bind(("0.0.0.0",server_port))
server_welcome_socket.listen(1)
print ('The server is ready to receive')

##creating the while loop
while True:
    print("waiting for connection establishment")
    connection_socket, client_add = server_welcome_socket.accept()
    print("connection successfull, processing request")
    
    ## now the date and time 
    now = datetime.utcnow()
    stamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    ##sending the stamp to client
    connection_socket.send(stamp.encode())

    ##finally close when job is done
    connection_socket.close()