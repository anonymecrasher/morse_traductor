import pygame
import api
import time


class Windows:
    def __init__(self):
        self.morse_time = api.MorseTime()
        pygame.mixer.init()
        self.bip_sonor = pygame.mixer.Sound("bip.wav") # il faudra ajouter un fichier sonnor en .ogg ou .wav

    def sounds(self, value: str):
        """
        :param value:(str type)
        :return None:

        Description FR:
            -Cette fonction est une procédure qui va a partir d'un texte en morse (exemple ... --- ...) le traduire en
            bip sonore de durer equivalante au morse.
        Description EN:
            -This function is a procedure that will translate a morse code text (example ... --- ...) into a
            beep sound of equivalent duration to morse code.
        """
        splited = api.split_morse(value)
        print(splited)
        for letter in splited:
            for symbol in letter:
                if symbol == ".":
                    self.bip_sonor.play()
                    time.sleep(self.morse_time.court)
                    self.bip_sonor.stop()
                    time.sleep(self.morse_time.very_short)
                elif symbol == "-":
                    self.bip_sonor.play()
                    time.sleep(self.morse_time.long)
                    self.bip_sonor.stop()
                    time.sleep(self.morse_time.very_short)
                elif symbol == "/":
                    time.sleep(self.morse_time.space)
            time.sleep(self.morse_time.court)


if __name__ == "__main__":
    traducteur_type = Windows()
    traducteur_type.sounds("TEST TEST TEST")