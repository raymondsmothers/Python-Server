import socket

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

#functions
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen()

#while True:
(client, address) = server_socket.accept()

while True:
    message = client.recv(1024).decode()
    if(message == 'bye'):
        client.close()
        server_socket.close()
    else:
        client.send(message.encode())
