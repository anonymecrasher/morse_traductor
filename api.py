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
                     "--.--": '''Ñ''', "---.": '''Ö''', "...-.": '''Ŝ''', ".--..": '''Þ''', "..--": '''Ü''',
                     '''/''': ''' '''}


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
                     '''Ñ''': "--.--",  '''Ö''': "---.",  '''Ŝ''': "...-.",  '''Þ''': ".--..", '''Ü''': "..--",
                     ''' ''': '''/'''}


def text_to_morse(value: str) -> str:
    """
    Encode a text message into a morse one.

    :param value: (str type)
    :return morse_code: (str type)
    """
    value = value.upper()
    morse_code = ""
    for i in range(len(value)):
        temp_value = str(ALPHABET_TO_MORSE[value[i]])

        morse_code = morse_code + " " + temp_value
    return morse_code.strip()


def morse_to_text(value: str) -> str:
    """
    Decode morse into text message.

    :param value: (str type)
    :return text_code: (str  type)
    """
    text_code = ""
    value = value.split(" ")
    for i in range(len(value)):
        temp_value = str(MORSE_TO_ALPHABET[value[i]])

        text_code = text_code + temp_value
    return text_code


def split_morse(value: str) -> list:
    """
    Encode a text message into a list of morse one.
    :param value: (str type)
    :return morse_code: (list type)
    """
    morse_code = text_to_morse(value)
    return morse_code.split()


def convert_button_time(button_time: list) -> str:
    """
    Convert the list of time into a symbol (morse)

    :param button_time: (list type), time in nanosecond
    :return symbol: (str type)
    """
    symbol = ""
    for i in button_time:
        if 1000000 <= i < 600000000:
            symbol = symbol + "."
        elif 600000000 <= i < 1300000000:
            symbol = symbol + "-"
        elif 1300000000 <= i < 2600000000:
            symbol = symbol + " "
        elif 2600000000 <= i:
            symbol = symbol + "/"
        else:
            raise ValueError
    return symbol


class MorseTime:
    def __init__(self, court: float = 0.2):
        """
        :param court: (float type)
        Description FR:
            -Ici l'objectif est de déclarer une liste de constantes qui serviront pour l'entiereté du programme, elles
            sont toutes proportionnelles à la varriable "court" donc si les temps ne vous conviennent pas vous pouvez
            changer la valeur de la variable "court".
        Description EN:
            -Here the objective is to declare a list of constants that will be used for the entire program, it
            are all proportional to the variable "court" so if the times do not suit you you can change
            the value of the "court" variable.

        """
        if court < 0:
            court = -court
        self.court = court
        self.long = self.court * 3
        self.space = self.court * 7
        self.very_short = court / 2

if __name__ == "__main__":
    print(text_to_morse("BONJOUR"))
    print(morse_to_text("... --- ..."))

