import time
from machine import Pin, SoftI2C
from default import api
import socket
import screen


def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('On a de la connection FIBRE', 'LmO3eE1cQctC$')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def my_local_ip():
    import network
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.ifconfig()[0]


class ESP32:
    def __init__(self, name: str, your_ip: str, port: int = 2236):
        self.morse_time = api.MorseTime()
        self.button_green = Pin(17, Pin.IN, Pin.PULL_UP)
        self.button_red = Pin(18, Pin.IN, Pin.PULL_UP)
        self.green_led = Pin(13, Pin.OUT)
        self.yellow_led = Pin(16, Pin.OUT)
        self.red_led = Pin(14, Pin.OUT)
        self.buzzer = Pin(4, Pin.OUT)
        self.i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        self.oled = screen.SSD1306_I2C(128, 64, self.i2c)

        # Network var
        # {"ip": ("username", 2236)} <- as an example
        self.target_ip = {}
        self.port = port
        self.name = name
        # Like 192.168.1.157
        self.device_ip = your_ip
        self.splited_ip = list(map(int, self.device_ip.split(".")))

    def light(self, morse: str):
        """
        Convert morse symbols to led signal
        :param value: (str type)
        :return None:
        """
        splited = morse.split()
        for word in splited:
            for symbol in word:
                if symbol == ".":
                    self.yellow_led.value(1)
                    time.sleep(self.morse_time.court)
                    self.yellow_led.value(0)
                    time.sleep(self.morse_time.very_short)
                elif symbol == "-":
                    self.yellow_led.value(1)
                    time.sleep(self.morse_time.long)
                    self.yellow_led.value(0)
                    time.sleep(self.morse_time.very_short)
                elif symbol == "/":
                    time.sleep(self.morse_time.space)
            time.sleep(self.morse_time.court)

    def get_button_time(self) -> list:
        """
        Get a list of timer in nanoseconds. From 1000000 to infinity
        :return elapsed_time: (list type)
        """
        elapsed_time = []
        time.sleep(1)
        print("Now you can push any button !")
        while True:
            if self.button_green.value() == 0:
                is_pressed = time.time_ns()
                while self.button_green.value() == 0:
                    while_pressed = time.time_ns()
                    result = while_pressed - is_pressed
                    if result > 1000000:
                        self.oled.fill(0)
                        self.oled.text(api.time_to_symbol(result), 64, 32)
                        self.oled.show()
                after_pressed = time.time_ns()
                result = after_pressed - is_pressed
                if result > 1000000:
                    self.oled.fill(0)
                    self.oled.show()
                    elapsed_time.append(result)
                    time.sleep(0.1)
            elif self.button_red.value() == 0:
                return elapsed_time

    def udp_scan(self, port: int = 2236, lock=False):
        """
        Scan all the Network to find if some device are UP to talk in Morse with UDP
        :param base_host: Your local IP -> 192.168.1.97 over the network
        :param port: the port you want to scan (2236)
        :return:
        """
        host_list = self.splited_ip
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ping_message = f"ping {self.name} {self.port}"
        for i in range(255):
            host_list[3] = i
            ip = ".".join(map(str, host_list))
            try:
                if self.device_ip != ip:
                    sock.sendto(ping_message.encode(), (ip, port))
            except OSError as e:
                print(f"{ip} except error: {e}")
            time.sleep(0.05)
        sock.close()

        if lock:
            lock.release()

    def udp_receiver(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.port))

        error = False
        while error is False:
            data, addr = sock.recvfrom(1024)
            data = data.decode()
            split = data.split(" ")
            if "ping" in data or "pong" in data:
                if addr[0] in self.target_ip:
                    print("user have already been accepted")
                    # We send the pong anyway, Maybe the peer lost connection and is scanning the network again
                    self.udp_sender(f"pong {self.name}", addr[0], self.port)
                    continue

                # Does hte ping contain a nickname -> ping timtonix
                if len(split) >= 2:
                    username = split[1]
                else:
                    username = "anonyme"

                print(f"{addr[0]} is {username}")
                if self.check_peer(username, addr[0], self.port) and "ping" in data:
                    self.udp_sender(f"pong {self.name}", addr[0], self.port)
                    print("ponged")
                elif self.check_peer(username, addr[0], self.port) and "pong" in data:
                    print("user accepted")
            else:
                if api.is_morse(data):
                    self.light(data)

    def check_peer(self, username, ip: str, port: int = 2236):
        # Afficher à l'écran
        self.oled.fill(0)
        self.oled.text(f"Found {username}", 0, 0)
        self.oled.text(ip, 0, 9)
        self.oled.text(f"Add -> Green", 0, 19)
        self.oled.text(f"Refuse -> Red", 0, 29)
        self.oled.show()

        while self.button_green.value() != 0 or self.button_red.value() != 0:
            if self.button_green.value() == 0:
                self.target_ip[ip] = (username, port)
                self.oled.fill(0)
                self.oled.text(f"{username}", 0, 0)
                self.oled.text(f"Accepted !", 0, 10)
                self.oled.show()
                return True
            elif self.button_red.value() == 0:
                self.oled.fill(0)
                self.oled.text(f"{username}", 0, 0)
                self.oled.text(f"Rejected !", 0, 10)
                self.oled.show()
                return False


    def udp_sender(self, message: str, host, port: int = 2236):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        request = f"{message}".encode()
        try:
            sock.sendto(request, (host, port))
        except OSError as e:
            print(e)


if __name__ == "__main__":
    do_connect()
    esp = ESP32("timtonix", my_local_ip())
    receiver = _thread.start_new_thread(esp.udp_receiver, ())
    scaner = _thread.start_new_thread(esp.udp_scan, ())
    while esp.target_ip == {}:
        pass
    print(esp.target_ip)





