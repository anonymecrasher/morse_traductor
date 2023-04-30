import api
import time
import RPi.GPIO as GPIO


class Raspberry:
    def __init__(self):
        self.morse_time = api.MorseTime()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

    def light(self, value: str):
        splited = api.text_to_morse(value)
        for word in splited:
            for symbol in word:
                if symbol == ".":
                    GPIO.output(5, GPIO.HIGH)
                    time.sleep(self.morse_time.court)
                    GPIO.output(5, GPIO.LOW)
                    time.sleep(self.morse_time.very_short)
                elif symbol == "-":
                    GPIO.output(5, GPIO.HIGH)
                    time.sleep(self.morse_time.long)
                    GPIO.output(5, GPIO.LOW)
                    time.sleep(self.morse_time.very_short)
            time.sleep(self.morse_time.court)


if __name__ == "__main__":
    traducteur_type = Raspberry()
    traducteur_type.light(input("quel est le texte que voulez vous afficher ?"))
