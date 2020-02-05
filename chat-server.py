#!/usr/bin/python

#import statements
import threading
import socket

#parameters
MAX_LIST_SIZE = 5

#global variables
client_list = []   #list of connected clients

#functions
def handle_input(mess, client):
    print("Needs work")
    return

def handle_disconnect(client):
	#check if the list is empty or the client exists
	if((client is None) or (not client_list)):
		return
	
	#send disconnect notification and
	#remove from client_list and close connection
	client.send(b'Disconnecting from server')
	client_list.remove(client)
	client.close()
	return

#TODO: implement the following handle input function
#def handle_input():

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

#accept loop
while True:
    #accept client and send indication to client
    (client, address) = server_socket.accept()
	
	#add client to the list of active clients
    client_list.append(client)
	
    print("Success!")
    
    #send client welcome message
    client.send(b'Thank you for connecting')
    
    #close the connection
    client.close()    
            
#done
print('terminating server...')

