import time
from machine import Pin
import api


class ESP32:
    def __init__(self):
        self.morse_time = api.MorseTime()
        self.button = Pin(17, Pin.IN, Pin.PULL_UP)
        self.led = Pin(16, Pin.OUT)

    def light(self, value: str):
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


if __name__ == "__main__":
    traducteur_type = ESP32()
    traducteur_type.light("TEST")
