from http import client
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 3000

serversocket.bind((host, port))
serversocket.listen(3)

msg = "Thank you for connecting" + "\r\n"

while True:
    clientsocket, address = serversocket.accept()
    print(f"Received connection from {str(address)}")

    clientsocket.send(msg.encode())
    clientsocket.close()
