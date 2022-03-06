import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3000

clientsocket.connect((host, port))
msg = clientsocket.recv(1024)
clientsocket.close()

print(msg.decode("ASCII"))
