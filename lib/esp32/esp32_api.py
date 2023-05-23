import time
from machine import Pin
import api
import socket


class ESP32:
    def __init__(self, your_ip: str, port: int = 2236):
        self.morse_time = api.MorseTime()
        self.button_green = Pin(17, Pin.IN, Pin.PULL_UP)
        self.button_red = Pin(18, Pin.IN, Pin.PULL_UP)
        self.led = Pin(16, Pin.OUT)

        # Network var
        self.target_ip = []
        self.port = port
        # Like 192.168.1.157
        self.device_ip = your_ip

    def light(self, value: str):
        """
        Convert morse symbols to led signal
        :param value: (str type)
        :return None:
        """
        splited = api.text_to_morse(value)
        for word in splited:
            for symbol in word:
                if symbol == ".":
                    self.led.value(1)
                    time.sleep(self.morse_time.court)
                    self.led.value(0)
                    time.sleep(self.morse_time.very_short)
                elif symbol == "-":
                    self.led.value(1)
                    time.sleep(self.morse_time.long)
                    self.led.value(0)
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
                    pass
                after_pressed = time.time_ns()
                result = after_pressed - is_pressed
                if result > 1000000:
                    elapsed_time.append(result)
                    time.sleep(0.1)
            elif self.button_red.value() == 0:
                return elapsed_time

    def receive_pong(self, lock):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("", self.port))
        discovered_host = False
        while discovered_host is False:
            data, temp_addr = sock.recvfrom(1024)
            data = data.decode()
            if "pong" in data:
                self.target_ip.append(temp_addr[0])
                discovered_host = True
                lock.release()

    def udp_scan(self, base_host: list, port: int = 2236):
        """
        Scan all the Network to find if some device are UP to talk in Morse with UDP
        :param base_host: Your local IP -> 192.168.1.97 over the network
        :param port: the port you want to scan (2236)
        :return:
        """
        base_host[3] = 0
        for i in range(255):
            base_host[3] = i
            ip = ".".join(map(str, base_host))
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                if self.device_ip != ip:
                    sock.sendto(b'ping', (ip, port))
            except OSError as e:
                print(f"{ip} except error: {e}")
            sock.close()
            time.sleep(0.05)


if __name__ == "__main__":

    esp = ESP32()
    while True:
        if esp.button_red.value() == 0:
            bla = api.convert_button_time(esp.get_button_time())
            print(api.morse_to_text(bla))
