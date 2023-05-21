import socket
import wifi
import network


wifi.do_connect()
sta_if = network.WLAN(network.STA_IF)
IP = sta_if.ifconfig()[0]
PORT = 2236

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))
print("socket actived")

while True:
    data, addr = sock.recvfrom(1024)
    if data.decode() == "ping":
        message = f"pong {IP}".encode()
        sock.sendto(message, (addr[0], PORT))
    else:
        print(data)


