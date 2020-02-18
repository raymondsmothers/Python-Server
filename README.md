# Python-Server

##Overview
Simple python3 TCP Chatroom server and client. Users will be able to connect to the server with the appropriate client and be able to send and receive messages to and from other clients connect to the server.

###Server Protocol
The server will be using Transmission Control Protocol (TCP) and clients must be able to exchange the appropriate protocol commands (simple strings) with the server in order to succesffuly connect. 

###Client
Each client will be associated with a unique username. Clients will be able to send messages in the form of an alphanumeric string whose length cannot exceed 100 characters.
