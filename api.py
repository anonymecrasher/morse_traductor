#!/usr/bin/env python
# -*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

# déclaration des constantes

n1 = 0
court = 0.2
long = court * 3
espace = court * 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

MORSE_TO_ALPHABET = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
                     "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
                     "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                     "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                     ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-.-.-": '''.''',
                     "--..--": ''',''', "..--..": '''?''', ".----.": """'""", "-.-.-----.": '''!''', "-..-.": '''/''',
                     "-.--.": '''(''', "-.--.-": ''')''', ".-...": '''&''', "---...": ''':''', "-.-.-.": ''';''',
                     "-...-": '''=''', ".-.-.": '''+''', "-....-": '''-''', "..--.-": '''_''', ".-..-.": '''"''',
                     "...-..-": '''$''', ".--.-.": '''@''', ".-.-": '''Ä''', ".--.-": '''À''', "-.-..": '''Ĉ''',
                     "..--.": '''Ð''', ".-..-": '''È''', "..-..": '''É''', "--.-.": '''Ĝ''', ".---.": '''Ĵ''',
                     "--.--": '''Ñ''', "---.": '''Ö''', "...-.": '''Ŝ''', ".--..": '''Þ''', "..--": '''Ü'''}


ALPHABET_TO_MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                     "I": "..", ".---": "J",  "K": "-.-", "L": ".-..", "M": "--", "N": "-.",  "O": "---", "P": ".--.",
                     "Q": "--.-", "R": ".-.", "S": "...",  "T": "-", "U": "..-",  "V": "...-", "W": ".--", "X": "-..-",
                     "Y": "-.--", "Z": "--..",  "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--", "4": "....-",
                     "5": ".....",  "6": "-....", "7": "--...",  "8": "---..", "9": "----.", '''.''': ".-.-.-",
                     ''',''': "--..--", '''?''': "..--..", """'""": ".----.", '''!''': "-.-.-----.", '''/''': "-..-.",
                     '''(''': "-.--.", ''')''': "-.--.-",  '''&''': ".-...",  ''':''': "---...", ''';''': "-.-.-.",
                     '''=''': "-...-",  '''+''': ".-.-.",  '''-''': "-....-", '''_''': "..--.-", '''"''': ".-..-.",
                     '''$''': "...-..-", '''@''': ".--.-.", '''Ä''': ".-.-", '''À''': ".--.-", '''Ĉ''': "-.-..",
                     '''Ð''': "..--.", '''È''': ".-..-", '''É''': "..-..", '''Ĝ''': "--.-.", '''Ĵ''': ".---.",
                     '''Ñ''': "--.--",  '''Ö''': "---.",  '''Ŝ''': "...-.",  '''Þ''': ".--..", '''Ü''': "..--"}


class MorseTrad:
    def __init__(self):
        pass







def longue(temps):
    """
    :param temps: (en input: "court" or "long")
    :return:
    description:
        fait clignoter un lampe "n" fois d'un temps "temps"
    """

    GPIO.output(5, GPIO.HIGH)
    time.sleep(temps)
    GPIO.output(5, GPIO.LOW)
    time.sleep(court)


# programme principal
texte = input("'entrez votre texte a traduire")