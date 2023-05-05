import time
from machine import Pin
import api


class ESP32:
    def __init__(self):
        self.morse_time = api.MorseTime()
        self.button_green = Pin(17, Pin.IN, Pin.PULL_UP)
        self.button_red = Pin(18, Pin.IN, Pin.PULL_UP)
        self.led = Pin(16, Pin.OUT)

    def light(self, value: str):
        """
        :param value: (str type)
        :return None:
        Description FR:
            -Cette fonction est une procédure qui va a partir d'un texte en morse (exemple ... --- ...) le traduire en
            signal lumineux de durer equivalante au morse.
        Description EN:
            -This function is a procedure that will translate a morse code text (example ... --- ...) into a
            light signal of equivalent duration to morse code.

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
        :return elapsed_time: (list type)
        Description FR:
            -Cette fonction va recuperer les temps d'appuis sur des bouton et va les renvoyer sous forme d'une liste
            des temps d'appuis.
        Description EN:
            -This function will retrieve the button press times and return them as a list of
            list of button presses.

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


if __name__ == "__main__":
    esp = ESP32()
    while True:
        if esp.button_red.value() == 0:
            bla = api.convert_button_time(esp.get_button_time())
            print(api.morse_to_text(bla))
