import socket

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

MAX_SIZE = 100

with socket.socket() as server_socket:
    server_socket.connect((HOST, PORT))

    print(server_socket.recv(MAX_SIZE).decode())

    while True:
        message = input()
        if(message == 'bye'):
            break
        else:
            server_socket.send(message.encode())
            print(server_socket.recv(MAX_SIZE).decode())
    
