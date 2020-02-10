import socket

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

MAX_SIZE = 100

protocol_server_init = '<chatroomserver>'
protocol_client_resp = '<chatroomclient>'
protocol_server_acpt = '<okconnection>'

def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((HOST, PORT))

        print(server_socket.recv(MAX_SIZE).decode())

        while True:
            message = input()
            if(message == 'bye'):
                break
            else:
                server_socket.send(message.encode())
                print(server_socket.recv(MAX_SIZE).decode())
                
def handle_protocol_ex(server):
    init_message = server.recv(1024).decode()
    if(init_message != protocol_server_init):
        return False
    server.send(
    
