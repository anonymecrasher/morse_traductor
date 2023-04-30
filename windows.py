import pygame
import api
import time

class windows:
    def __init__(self):
        self.morse_time = api.MorseTime()
        self.bip_sonor = pygame.mixer.Sound("bip.wav")
    def sons_up(self, temps):
        self.bip_sonor.play()
        time.sleep(temps)
        self.bip_sonor.stop()
        time.sleep(self.morse_time.court)
    def show_morse_code(self, value: str):
        morse_code = api.text_to_morse(value)
        morse_table = morse_code.split(" ")
        for letter in morse_table:
            for i in letter:
                if i == ".":
                    self.sons_up(self.morse_time.court)
                elif i == "-":
                    self.sons_up(self.morse_time.long)
            time.sleep(self.morse_time.court)

if __name__ == "__main__":
    traducteur_type = windows()
    traducteur_type.show_morse_code("TEST")