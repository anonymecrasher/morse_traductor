import socket

PORT = 2236

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))
print("socket actived")

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == "ping":
        print(f"pinged by {addr[0]}")
        message = f"ping".encode()
        sock.sendto(message, (addr[0], PORT))
    else:
        print(data)
