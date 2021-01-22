import socket as s
from auxiliary import *

server_name = '192.168.100.13'
server_port = 12000
buffer_size = 2048

msg = input("Input a lowercase sentence: ")
msg = str_to_bytes(msg)

client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)
client_socket.sendto(msg, (server_name, server_port))
client_socket.settimeout(3)

try:
    srv_msg, server_address = client_socket.recvfrom(buffer_size)
except s.timeout:
    print("Server didn't respond...")
    exit(1)

srv_msg = bytes_to_str(srv_msg)
print("Received from server:", srv_msg)
print("Server address:", server_address)
client_socket.close()
