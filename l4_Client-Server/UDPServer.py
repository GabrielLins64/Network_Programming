import socket as s
from auxiliary import *
from signal import signal, SIGINT

def handler(signal_received, frame):
    global server_socket
    server_socket.close()
    print("\nClosing server. Goodbye!")
    exit(0)

# server_IP = "192.168.100.13"
server_port = 12000
buffer_size = 2048
signal(SIGINT, handler)

server_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
server_socket.bind(('', server_port))

print("##################")
print("## GabServer =) ##")
print("##################")
print("Server has started!")
print("Server IP:", s.gethostbyname(s.gethostname() + ".local"))
print("Listening on port", server_socket.getsockname()[1])
print()

while (True):
    client_msg, client_addr = server_socket.recvfrom(buffer_size)

    msg = bytes_to_str(client_msg)
    print("Received:", msg)
    print("From:", client_addr)

    msg = msg.upper()
    msg = str_to_bytes(msg)

    server_socket.sendto(msg, client_addr)
