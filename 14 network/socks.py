import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("www.python.org", 80))

# s.listen(10)


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.1", 80))
    sock.listen(5)
    sock.accept()

def client():
    sock = socket.socket()
    sock.connect(("192.168.1.1", 80))