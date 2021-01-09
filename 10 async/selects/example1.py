import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.setblocking(0)
socks = [sock]
sock.connect(("localhost", 8888))
sock.sendall(input().encode())
readable, _, _ = select.select(socks, [], [], 60)
for s in readable:
    print(s.recv(1024))