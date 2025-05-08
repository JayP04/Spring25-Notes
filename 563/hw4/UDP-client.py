##code is similar to tcp clientfile.

import socket
import datetime
import time
import sys


def start_client(server_ip, server_port):

    ## initializing UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        #setting a timeout to handle packet loss or network issues
        client_socket.settimeout(2)  # Timeout in seconds

        request_sent_time = time.time()  ## recording the time sent
        client_socket.sendto(b"REQUEST_TIME", (server_ip, server_port)) ## sending request to the server

        try:
            stamp, server_address = client_socket.recvfrom(1024)  ## receiving data from the server
            stamp = stamp.decode('utf-8')  ## decoding server response

            response_received_time = time.time()  ## record the receive time
            rtt = (response_received_time - request_sent_time) * 1000  ## calculating the round trip time in milliseconds

            try:  ## to ensure that timestamp format is right on the server side
                server_time = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%S.%fZ")
            except:
                print("Error: time stamp format is incorrect")
                return

            local_time = datetime.datetime.utcnow()

            # now calculating the client-to-server delay
            client_to_server_delay = (rtt / 2)  ## one way
            time_difference = (local_time - server_time).total_seconds() * 1000  # in milliseconds

            # printing for easier readability
            print(f"Timestamp of server: {stamp}\n")
            print(f"Current local time of client: {local_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')}\n")
            print(f"Time difference: {time_difference:.3f} ms\n")
            print(f"RTT: {rtt:.3f} ms\n")
            print(f"Approximate delay from Client-to-server: {client_to_server_delay:.3f} ms\n")

        except socket.timeout:
            print("Error: Request timed out. No response from server.")
            return

    finally:
        client_socket.close()


## conditioning the usage statement
if len(sys.argv) != 3:
    print("Usage: python UDP-client.py <server-ip-address> <server-port-number>")
    sys.exit(1)


server_ip = sys.argv[1]
server_port = int(sys.argv[2])
start_client(server_ip, server_port)
