from socket import *
from auxiliary import *

server_name = '192.168.100.13'
server_port = 12000
buffer_size = 1024

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

msg = input("Input a lowercase sentence: ")
msg = str_to_bytes(msg)

client_socket.send(msg)
srv_msg = client_socket.recv(buffer_size)

srv_msg = bytes_to_str(srv_msg)
print("Received from server:", srv_msg)
client_socket.close()
