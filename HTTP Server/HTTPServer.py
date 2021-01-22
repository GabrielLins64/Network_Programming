from socket import *
import sys
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
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
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
    connection_socket, addr = server_socket.accept()
    connection_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    print("TCP Connection established with", addr)

    try:
        msg = connection_socket.recv(buffer_size).decode()
        print(msg)
        if(msg==""):
            connection_socket.close()
            continue
        requested_file = msg.split()[1]
        if(requested_file=='/'): requested_file = '/index.html'
        file = open(requested_file[1:], 'r')
        data = file.read()
        file.close()

        HTTP_response = "HTTP/1.1 200 OK\n"
        HTTP_response += "Content-Type: text/html\n"
        HTTP_response += "Connection: Closed\r\n"

        try:
            connection_socket.send(HTTP_response.encode())
            connection_socket.send("\r\n".encode())
            for line in data:
                connection_socket.send(line.encode())
            connection_socket.send("\r\n".encode())
        except BrokenPipeError:
            print("Connection could not be stablished with:", addr)
            connection_socket.close()
            continue
    
    except IOError:
        file = open("notfound.html", "r")
        data = file.read()
        file.close()
        
        HTTP_response = "HTTP/1.1 404 Not Found\n"
        HTTP_response += "Content-Type: text/html\n"
        HTTP_response += "Connection: Closed\r\n"
        connection_socket.send(HTTP_response.encode())
        connection_socket.send("\r\n".encode())
        for line in data:
            connection_socket.send(line.encode())
        connection_socket.send("\r\n".encode())

    connection_socket.close()
    print("TCP Connection closed with", addr)
        