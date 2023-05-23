import socket
import _thread
import wifi
import time
import network

wifi.do_connect()
sta_if = network.WLAN(network.STA_IF)
esp_ip = sta_if.ifconfig()[0]

LOCAL_IP = [192, 168, 1, 1]
addr = ""


def send_udp_ping(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(b'ping', (host, port))
    except OSError as e:
        print(f"{host} except error: {e}")
    sock.close()


def receive_pong(lock):
    global addr
    print(addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 2236))
    discovered_host = False
    while discovered_host is False:
        data, addr = sock.recvfrom(1024)
        data = data.decode()
        if "pong" in data:
            addr = addr[0]
            discovered_host = True
            lock.release()
        else:
            data = ""
            addr = ""


if __name__ == "__main__":
    s_time = time.time()
    lock = _thread.allocate_lock()
    lock.acquire()
    receiver = _thread.start_new_thread(receive_pong, (lock,))
    for i in range(255):
        LOCAL_IP[3] = i
        ip = ".".join(map(str, LOCAL_IP))
        if ip != esp_ip:
            send_udp_ping(ip, 2236)
            time.sleep(0.05)
        else:
            print("handled")
    print("end")

    while lock.locked():
        n_time = time.time()
        if n_time - s_time >= 10:
            discovered_host = True
            lock.release()
            print("No available device")

    if addr != "":
        print(f"The target device is {addr}")
