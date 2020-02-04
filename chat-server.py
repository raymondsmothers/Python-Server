#!/usr/bin/python

#import statements
import threading
import socket

#global variables
client_list = []   #list of connected clients

#functions
#def handle_client(socket):
    

#def handle_thread():
    

def handle_input()        


#create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get machine ip address
server_ip = socket.gethostname()

#port for client access
port = 12345

#bind socket
server_socket.bind((server_ip, port))

#listen for client connections
server_socket.listen()

while True:
    #accept client and send indication to client
    (client, address) = server_socket.accept()
    print("Success!")
    
    #send client welcome message
    client.send(b'Thank you for connecting')
    
    #close the connection
    client.close()    
            
#done
print('terminating server...')
