import socket


def main():
    ip = input("The IP: ")
    port = input("The port: ")

    bannergrab(ip, int(port))


def bannergrab(ip: str, port: int):
    s = socket.socket()
    s.connect((ip, port))
    s.settimeout(5)
    response = s.recv(1024)

    print("")
    print(response.decode())


main()
