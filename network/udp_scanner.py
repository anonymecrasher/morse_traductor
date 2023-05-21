import socket
import threading
from ipaddress import ip_network

LOCAL_IP = ip_network("192.168.1.0/24")
addr = ""


def send_udp_ping(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"send to {host}")
    try:
        sock.sendto(b'ping', (host, port))
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


if __name__ == "__main__":
    receiver = threading.Thread(target=receive_pong)
    receiver.start()
    for ip in LOCAL_IP:
        sender = threading.Thread(target=send_udp_ping, args=(str(ip), 2236,))
        sender.start()
    receiver.join()
    if addr != "":
        print(f"The target device is {addr}")