import pygame
import api
import time

class windows:
    def __init__(self):
        self.morse_time = api.MorseTime()
        pygame.mixer.init()
        self.bip_sonor = pygame.mixer.Sound("bip.wav") # il faudra ajouter un fichier sonnor en .ogg ou .wav

    def sons_up(self, temps):
        self.bip_sonor.play()
        time.sleep(temps)
        self.bip_sonor.stop()
        time.sleep(self.morse_time.court)

    def show_morse_code(self, value: str):
        morse_code = api.text_to_morse(value)
        morse_table = []
        i = 0
        n = 0
        while i < len(morse_code):
            if morse_code[i] != " ":
                morse_table.append(morse_code[i])
                n = 0
            elif morse_code[i] == " ":
                n += 1
                if n == 1:
                    pass
                elif n == 2:
                    n = 0
                    morse_table.append(" ")
                    i += 1

            i += 1
        for letter in morse_table:
            for i in letter:
                if i == ".":
                    self.sons_up(self.morse_time.court)
                elif i == "-":
                    self.sons_up(self.morse_time.long)
                elif i == " ":
                    time.sleep(self.morse_time.space)
            time.sleep(self.morse_time.court)


if __name__ == "__main__":
    traducteur_type = windows()
    traducteur_type.show_morse_code("TEST TEST")