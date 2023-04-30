import api
import time
import RPi.GPIO as GPIO


class Raspberry:
    def __init__(self):
        self.traducteur = api.MorseTrad()
        self.court = 0.2
        self.long = self.court * 3
        self.espace = self.court * 7
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

    def light_up(self, temps):
        GPIO.output(5, GPIO.HIGH)
        time.sleep(temps)
        GPIO.output(5, GPIO.LOW)
        time.sleep(self.court)

    def show_morse_code(self, value: str):
        morse_code = self.traducteur.text_to_morse(value)
        morse_table = morse_code.split(" ")
        for letter in morse_table:
            for i in letter:
                if i == ".":
                    self.light_up(self.court)
                elif i == "-":
                    self.light_up(self.long)

    def get_text_to_show(self):
        pass


if __name__ == "__main__":
    traducteur_type = Raspberry()
    traducteur_type.show_morse_code(input("quel est le texte que voulez vous afficher ?"))
