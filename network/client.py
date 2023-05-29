import socket
import api


PORT = 2236

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))
print("socket actived")

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode()
    if "ping" in data:
        data = data.split(" ")
        print(f"pinged by {addr[0]} {data[1]}")
        message = f"pong server {PORT}".encode()
        sock.sendto(message, (addr[0], PORT))
    else:
        print(data)
        print(f"converted message : {api.morse_to_text(data)}")