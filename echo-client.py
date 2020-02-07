import socket

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023


server_socket = socket.socket()

server_socket.connect((HOST, PORT))

while True:
    message = input()
    if(message == 'bye'):
        server_socket.close()
    else:
        server_socket.send(message.encode())
        print(server_socket.recv(1024).decode())
    
