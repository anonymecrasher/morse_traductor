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
                     "I": "..", "J": ".---",  "K": "-.-", "L": ".-..", "M": "--", "N": "-.",  "O": "---", "P": ".--.",
                     "Q": "--.-", "R": ".-.", "S": "...",  "T": "-", "U": "..-",  "V": "...-", "W": ".--", "X": "-..-",
                     "Y": "-.--", "Z": "--..",  "0": "-----",  "1": ".----",  "2": "..---",  "3": "...--", "4": "....-",
                     "5": ".....",  "6": "-....", "7": "--...",  "8": "---..", "9": "----.", '''.''': ".-.-.-",
                     ''',''': "--..--", '''?''': "..--..", """'""": ".----.", '''!''': "-.-.-----.", '''/''': "-..-.",
                     '''(''': "-.--.", ''')''': "-.--.-",  '''&''': ".-...",  ''':''': "---...", ''';''': "-.-.-.",
                     '''=''': "-...-",  '''+''': ".-.-.",  '''-''': "-....-", '''_''': "..--.-", '''"''': ".-..-.",
                     '''$''': "...-..-", '''@''': ".--.-.", '''Ä''': ".-.-", '''À''': ".--.-", '''Ĉ''': "-.-..",
                     '''Ð''': "..--.", '''È''': ".-..-", '''É''': "..-..", '''Ĝ''': "--.-.", '''Ĵ''': ".---.",
                     '''Ñ''': "--.--",  '''Ö''': "---.",  '''Ŝ''': "...-.",  '''Þ''': ".--..", '''Ü''': "..--"}


def text_to_morse(value: str) -> str:
    morse_code = ""
    for i in range(len(value)):
        temp_value = str(ALPHABET_TO_MORSE[value[i]])

        morse_code = morse_code + " " + temp_value
    return morse_code


def morse_to_text(value: str) -> str:
    text_code = ""
    value = value.split(" ")
    for i in range(len(value)):
        temp_value = str(MORSE_TO_ALPHABET[value[i]])

        text_code = text_code + temp_value
    return text_code


class MorseTime:
    def __init__(self, court: float = 0.2):
        self.court = court
        self.long = self.court * 3
        self.space = self.court * 7


if __name__ == "__main__":
    print(text_to_morse("BONJOUR"))
    print(morse_to_text("... --- ..."))

