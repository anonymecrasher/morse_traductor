import socket
import api
import netifaces
import threading
import os


def get_hostname() -> list:
    host = []
    for interface in netifaces.interfaces():
        if interface == "lo" or "vbox" in interface:
            continue
        details = netifaces.ifaddresses(interface)
        host.append(details[netifaces.AF_INET][0]["addr"])
    return host


class UDPClient:
    def __init__(self, port):
        self.port = port
        self.client_ip = get_hostname()


    def scanner(self):
        pass

    def receiver(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.port))
        print("Receiver have been bound !")
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode("utf-8")
            if "ping" in data:
                host = addr[0]
                data = data.split(" ")
                print(f"pinged by {addr[0]} {data[1]}")
                message = f"pong server {self.port}".encode()
                sock.sendto(message, (addr[0], self.port))
            elif "pong" in data:
                data = data.split(" ")
                print(f"Ponged by {data[1]}")
                print(data)
            else:
                print(data)
                print(f"converted : {api.morse_to_text(data)}")



if __name__ == "__main__":
    client = UDPClient(2236)
    print(client.client_ip)