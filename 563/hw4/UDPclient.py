import socket
import datetime
import time

def start_client(server_ip, server_port):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for receiving the response (in seconds)
    client_socket.settimeout(2)  # Timeout after 2 seconds if no response
    
    # Record the time when the request is sent
    request_sent_time = time.time()

    try:
        # Send a request to the server (just a placeholder request)
        client_socket.sendto(b"REQUEST_TIME", (server_ip, server_port))

        # Try to receive the response from the server
        try:
            timestamp, server_address = client_socket.recvfrom(1024)
            timestamp = timestamp.decode('utf-8')

            # Record the time when the response is received
            response_received_time = time.time()

            # Calculate the round-trip time (RTT) in milliseconds
            rtt = (response_received_time - request_sent_time) * 1000

            # Parse the timestamp string received from the server
            server_time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")

            # Get the current local time at the client
            local_time = datetime.datetime.utcnow()

            # Calculate the client-to-server delay (in milliseconds)
            client_to_server_delay = (rtt / 2)  # Assumption: RTT = 2 * client-to-server delay
            time_difference = (local_time - server_time).total_seconds() * 1000  # in milliseconds

            # Output the result
            print(f"Server timestamp: {timestamp}")
            print(f"Client local time: {local_time.strftime('%Y-%m-%dT%H:%M:%S.%fZ')}")
            print(f"Time difference (latency): {time_difference:.3f} ms")
            print(f"Round-trip time (RTT): {rtt:.3f} ms")
            print(f"Client-to-server delay (approx): {client_to_server_delay:.3f} ms")
        
        except socket.timeout:
            print("Error: No response from server. Packet loss or timeout occurred.")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python UDP-client.py <server-ip-address> <server-port-number>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
