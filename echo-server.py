#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
TCP Chatroom Server
Author: Raymond Smothers
'''

import socket
import threading

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

MAX_SIZE = 100
NAME_SIZE = 10
BREAK_STR = 'bye'

#protocols
protocol_server_init = '<chatroomserver>'
protocol_client_resp = '<chatroomclient>'
protocol_server_acpt = '<okconnection>'
protocol_err = '<protocolerror>'

#classes
class Client:
    def __init__(self, name, client_fd, client_address):
        self.name = name
        self.client_fd = client_fd
        self.client_address = client_address
        
#global
client_list = []

#functions
def handle_connections(server_socket):
    while True:
        (new_client, nc_address) = server_socket.socket()
        client_name = handle_proc_ex(new_client)
        
        new_client_obj = Client(client_name, new_client, nc_address)
        client_list.append(new_client_obj)
        

def handle_prot_ex(client):
    client_name = None
    client.send(protocol_server_init.encode())
    resp = client.recv(1024).decode()
    if(resp != protocol_client_resp):
        client.send(protocol_err.encode())
        client.close()
    else:
        client.send(protocol_server_acpt.encode())
        client_name = client.recv(NAME_SIZE).decode()
    return client_name

def init_server:  
    #with ensures that the resources are released upon termination 
    #also makes the code cleaner
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: 
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        #while True:
        (client, address) = server_socket.accept()

        prompt = 'Enter ' + BREAK_STR + ' to end session'
        client.send(prompt.encode())

        #x = threading.Thread(target=thread_function, args=(1,))
        thread = threading.Thread(target=handle_connection, None)

        while True:
            message = client.recv(MAX_SIZE).decode()
            if(message == BREAK_STR):
                break
            else:
                client.send(message.encode())

def main():
    init_server()   

if(__name__ == "__main__"):
    main()
