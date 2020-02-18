#!/usr/bin/env python3
#-*- coding: utf- -*-

'''
TCP Chatroom Client
Author: Raymond Smothers

Last Update: February 2020
'''

import socket

#constants
HOST = '127.0.0.1' #address of local machine
PORT = 6000        #non-priviledged ports are > 1023

#max message size
MAX_SIZE = 100

#protocols
protocol_server_init = '<chatroomserver>'
protocol_client_resp = '<chatroomclient>'
protocol_server_acpt = '<okconnection>'

#Description: Connect to the server
def connect_to_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect((HOST, PORT))

        print(server_socket.recv(MAX_SIZE).decode())
        handle_protocol_ex(server_socket)
        
        while True:
            message = input()
            if(message == 'bye'):
                break
            else:
                server_socket.send(message.encode())
                print(server_socket.recv(MAX_SIZE).decode())
                
#Description: Handle the protocol exchange with the server
#Returns: boolean based on if the exchange was successful or not
def handle_protocol_ex(server):
    init_message = server.recv(1024).decode()
    if(init_message != protocol_server_init):
        return False
    server.send(protocol_client_resp).encode()
    server_acpt = server.recv(1024).decode()
    if(server_acpt != protocol_server_acpt):
        return False
    else:
        getnsend_name(server)
	return True

#Description: Get client name and send it to the server
def getnsend_name(server_sock):
    client_name = None
    while len(client_name) > 10:
        client_name = input("What is your name? (10 or fewer characters may be used)")
    
    server_sock.send(client_name).encode()

#main function
def main():
    connect_to_server()

if(__name__ == "__main__"):
    main()
