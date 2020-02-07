import socket
import threading

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

MAX_SIZE = 100
BREAK_STR = 'bye'

#functions
def handle_connections():
    while True:
        
#with ensures that the resources are released upon termination 
#also makes the code cleaner
with socket.socket() as server_socket: 
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    #while True:
    (client, address) = server_socket.accept()

    prompt = 'Enter ' + BREAK_STR + ' to end session'
    client.send(prompt.encode())

    #x = threading.Thread(target=thread_function, args=(1,))
    thread = threading.Thread(target=handle_connection, null)

    while True:
        message = client.recv(MAX_SIZE).decode()
        if(message == BREAK_STR):
            break
        else:
            client.send(message.encode())
