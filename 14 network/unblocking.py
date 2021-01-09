import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("localhost", 8888))
socket.listen(100)
socket.setblocking(0)

try:
    client, addr = socket.accept()
except socket.error: # когда данных нет
    pass
else: # когда есть данные
    client.setblocking(0)
    pass
