import socket
import api
import threading

PORT = 2236


def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORT))
    print("socket actived")
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode("utf-8")
        if "ping" in data:
            host = addr[0]
            data = data.split(" ")
            print(f"pinged by {addr[0]} {data[1]}")
            message = f"pong server {PORT}".encode()
            sock.sendto(message, (addr[0], PORT))
        elif "pong" in data:
            data = data.split(" ")
            print(f"Ponged by {data[1]}")
            print(data)
        else:
            print(data)
            print(f"converted : {api.morse_to_text(data)}")


def send_message(message: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), ("192.168.1.157", 2236))


if __name__ == "__main__":
    receive = threading.Thread(target=receiver, args=[])
    receive.start()
    while True:
        print("You can send a message")
        message = input(">")
        send_message(message)