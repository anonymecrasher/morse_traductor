import socket
import default.api as api
import netifaces
import time


def get_hostname() -> list:
    host = []
    for interface in netifaces.interfaces():
        if interface == "lo" or "vbox" in interface:
            continue
        details = netifaces.ifaddresses(interface)
        host.append(details[netifaces.AF_INET][0]["addr"])
    return host


class UDPClient:
    def __init__(self, name, port: int = 2236, reachable: str = "on", discoverable: str = "on"):
        self.name = name
        self.port = port
        self.client_ip = get_hostname()
        self.split_ip = list(map(int, self.client_ip[0].split(".")))
        self.peers = {}
        self.discoverable = discoverable
        self.reachable = reachable

    def scanner(self):
        host_list = self.split_ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ping_message = f"ping {self.name} {self.port}"
        for i in range(255):
            host_list[3] = i
            ip = ".".join(map(str, host_list))
            try:
                if self.client_ip[0] != ip:
                    sock.sendto(ping_message.encode(), (ip, self.port))
            except OSError as e:
                print(f"{ip} except an error : {e}")
            time.sleep(0.05)
        sock.close()

    def receiver(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.port))
        print("Receiver have been setup !")
        while True:
            data, addr = sock.recvfrom(1024)
            data = data.decode("utf-8")
            if "ping" in data:
                self.handle_ping(addr, sock)
            elif "pong" in data:
                data = data.split(" ")
                print(f"Ponged by {data[1]}")
            else:
                print(data)
                print(f"converted : {api.morse_to_text(data)}")

    def sender(self, message: str, ip: str, port: int = 2236):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        request = f"{message}".encode()
        try:
            sock.sendto(request, (ip, port))
        except OSError as e:
            print(e)

    def add_peer(self, pseudo: str, ip: str, port: int):
        if ip != self.client_ip:
            self.peers[ip] = (pseudo, port)

    def handle_ping(self, addr: tuple, sock: object):
        message = f"pong server {self.port}".encode()
        sock.sendto(message, (addr[0], self.port))

if __name__ == "__main__":
    client = UDPClient("timtonix", 2236)
    print(client.client_ip)
    client.receiver()