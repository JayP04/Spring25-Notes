import socket
import datetime
import time
import sys



def start_client(server_ip, server_port):

    ## initializing TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:

        client_socket.connect((server_ip, server_port))
        request_sent_time = time.time() ## recording the time sent
        client_socket.sendall(b"REQUEST_TIME") ## sending request to the server
        stamp = client_socket.recv(1024).decode('utf-8')## to recieve from the server as utf8

        response_received_time = time.time()##record the recieve time
        rtt = (response_received_time - request_sent_time) * 1000 ## calculating the round trip time in milisecond

        try:##to ensure that timestamp format is right on the server side
            server_time = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%S.%fZ") 
        except:
            print("Error: time stamp format is incorrect")
            return
        
        local_time = datetime.datetime.utcnow()

        # now callculating  the client-to-server delay
        client_to_server_delay = (rtt / 2)  ## one way 
        time_difference = (local_time - server_time).total_seconds() * 1000  # in milliseconds

        #i will just print the results in one shot for easier readability. 
        print(f"Timestamp of server: {stamp}\n")
        print(f"Current locak time of client: {local_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')}\n")
        print(f"Time difference : {time_difference:.3f} ms\n")
        print(f"RTT: {rtt:.3f} ms\n")
        print(f"approximate dleay from Client-to-server : {client_to_server_delay:.3f} ms\n")
    
    finally:##got to know i can use finally with try!
        client_socket.close()

## conditining the usage statement. 
if len(sys.argv) != 3:
    print("Usage: python TCP-client.py <server-ip-address> <server-port-number>")
    sys.exit(1)


server_ip = sys.argv[1]
server_port = int(sys.argv[2])
start_client(server_ip, server_port)
