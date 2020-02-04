import socket

s = socket.socket()

host_machine = socket.gethostname()
port = 12345

s.connect((host_machine, port))
print(s.recv(1024).decode())
s.close()
