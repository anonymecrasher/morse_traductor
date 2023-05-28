import socket
import threading
from ipaddress import ip_network

LOCAL_IP = [192, 168, 1, 1]
addr = ""


def send_udp_ping(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"send to {host}")
    try:
        sock.sendto(b'ping server 2236', (host, port))
    except OSError:
        print(f"{host} except error")
    sock.close()


def receive_pong():
    global addr
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 2236))
    discovered_host = False

    while discovered_host is False:
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        if "pong" in data:
            addr = addr[0]
            discovered_host = True


def send_message(message: str, host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    request = message.encode()
    try:
        sock.sendto(request, (host, port))
    except OSError:
        print("Mon vieux t mort")

if __name__ == "__main__":
    """receiver = threading.Thread(target=receive_pong)
    receiver.start()
    for i in range(255):
        LOCAL_IP[3] = i
        ip = ".".join(map(str, LOCAL_IP))
        sender = threading.Thread(target=send_udp_ping, args=(str(ip), 2236,))
        sender.start()
    receiver.join()
    if addr != "":
        print(f"The target device is {addr}")"""
    send_udp_ping("192.168.1.157", 2236)
    send_message("--- ... ---", "192.168.1.157", 2236)