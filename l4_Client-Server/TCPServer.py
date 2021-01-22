from socket import *
from auxiliary import *
from signal import signal, SIGINT

def handler(signal_received, frame):
    global server_socket
    server_socket.close()
    print("\nClosing server. Goodbye!")
    exit(0)

server_port = 12000
buffer_size = 1024
signal(SIGINT, handler)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print("##################")
print("## GabServer =) ##")
print("##################")
print("Server has started!")
print("Server IP:", gethostbyname(gethostname() + ".local"))
print("Listening on port", server_socket.getsockname()[1])
print()

while(True):
    connection_socket, client_addr = server_socket.accept()
    msg = connection_socket.recv(buffer_size)
    msg = bytes_to_str(msg)
    print("Received:", msg)
    print("From:", client_addr)

    msg = msg.upper()
    msg = str_to_bytes(msg)

    connection_socket.send(msg)
    connection_socket.close()