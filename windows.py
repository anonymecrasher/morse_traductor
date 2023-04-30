import pygame
import api
import time

class windows:
    def __init__(self):
        self.morse_time = api.MorseTime()
        pygame.mixer.init()
        self.bip_sonor = pygame.mixer.Sound("bip.wav") # il faudra ajouter un fichier sonnor en .ogg ou .wav

    def sounds(self, value: str):
        splited = api.text_to_morse(value)
        for word in splited:
            for symbol in word:
                if symbol == ".":
                    self.bip_sonor.play()
                    time.sleep(self.morse_time.court)
                    self.bip_sonor.stop()
                    time.sleep(0.1)
                elif symbol == "-":
                    self.bip_sonor.play()
                    time.sleep(self.morse_time.long)
                    self.bip_sonor.stop()
                    time.sleep(self.morse_time.court)
            time.sleep(self.morse_time.court)


if __name__ == "__main__":
    traducteur_type = windows()
    traducteur_type.sounds("TEST")