import socket

#create the socket
s = socket.socket()

#get the address of the socket we want to connect to and port number
##NOTE: in this situation the address is the same as the host address##
host_machine = socket.gethostname()
port = 12345

#connect to the server
s.connect((host_machine, port))

#receive data
print(s.recv(1024).decode())

#close the connection
s.close()
