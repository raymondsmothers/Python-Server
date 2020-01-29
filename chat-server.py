#imports

#global variables

if(__name__ == "__main__"):
	#create the socket
	server_socket = socket.socket()
	
	#get local machine name
	host_machine = socket.gethostname()
	
	#get port number
	#this is the port clients will connect to
	port = 12345
	
	#bind port
	server_socket.bind((host, port))