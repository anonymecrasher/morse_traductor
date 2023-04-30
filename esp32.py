import time
from machine import Pin
import api


class ESP32:
    def __init__(self):
        self.traducteur = api.MorseTrad()
        self.court = 0.2
        self.long = self.court * 3
        self.espace = self.court * 7
        self.button = Pin(17, Pin.IN, Pin.PULL_UP)
        self.led = Pin(16, Pin.OUT)

    def light_up(self, temps):
        self.led.value(1)
        time.sleep(temps)
        self.led.value(0)
        time.sleep(self.court)

    def show_morse_code(self, value: str):
        morse_code = self.traducteur.text_to_morse(value)
        morse_table = morse_code.split(" ")
        for letter in morse_table:
            for i in letter:
                if i == ".":
                    self.light_up(self.court)
                elif i == "_":
                    self.light_up(self.long)

    def get_text_to_show(self):
        pass


if __name__ == "__main__":
    traducteur_type = ESP32()
    traducteur_type.show_morse_code("TEST")
