import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5050))
client = []
print('Start Server')
while 1:
    data, addr = sock.recvfrom(1024)
    print(addr[0], addr[1])
    if addr not in client:
        client.append(addr)
    for clients in client:
        if clients == addr:
            continue
        sock.sendto(data, clients)
