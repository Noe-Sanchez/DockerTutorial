# server.py

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server_socket.bind(('localhost', 12345))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    message = client_socket.recv(1024).decode()
    print("Server received: ", message)
    message = "Hello from server!"
    print("Sending to client: ", message)
    client_socket.send(message.encode())
    client_socket.close()
    break
