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
    :param value: (str type)
    :return morse_code: (str type)
    Description FR:
        -Cette fonction traduit un text "value" en morse grace a la bibliotech "ALPHABET_TO_MORSE".
        (exemple SOS ->  ... --- ...)
        -Cette fonction peut prendre en compte casiment toute les lettre de l'alphabet, les nombre, la ponctuation et
        aussi la casi totalité des caractere spéciaux (meme si il est fortement déconseiller de les utilliser).
    Description EN:
        -This function translates a "value" text into morse thanks to the "ALPHABET_TO_MORSE" library.
        (example SOS -> ... --- ...)
        -This function can take into account all the letters of the alphabet, numbers, punctuation and
        also all of the special characters (even if it is strongly advised not to use them).

    """
    value = value.upper()
    morse_code = ""
    for i in range(len(value)):
        temp_value = str(ALPHABET_TO_MORSE[value[i]])

        morse_code = morse_code + " " + temp_value
    return morse_code.strip()


def morse_to_text(value: str) -> str:
    """
    :param value: (str type)
    :return text_code: (str  type)
    Description FR:
        -Cette fonction traduit le code mosre "value" en text grace a la bibliotech "MORSE_TO_ALPHABET".
        (exemple ... --- ... ->  SOS)
        -Cette fonction peut prendre en compte casiment toute les lettre de l'alphabet, les nombre, la ponctuation et
        aussi la casi totalité des caractere spéciaux (meme si il est fortement déconseiller de les utilliser).
        -ATTENTION nous uttilison le carractere "/" pour signifier un espace entre deux mots et nous utilison le
        caractere " " pour signifier un changement de lettre.
    Description EN:
        -This function translates the mosre "value" code into text thanks to the "MORSE_TO_ALPHABET" library.
        (example ... --- ... -> SOS)
        -This function can take into account all the letters of the alphabet, numbers, punctuation and
        also all of the special characters (even if it is strongly advised not to use them).
        -ATTENTION we use the character "/" to mean a space between two words and we use the
        character " " to signify a change of letter.

    """
    text_code = ""
    value = value.split(" ")
    for i in range(len(value)):
        temp_value = str(MORSE_TO_ALPHABET[value[i]])

        text_code = text_code + temp_value
    return text_code


def split_morse(value: str) -> list:
    """
    :param value: (str type)
    :return morse_code: (list type)
    Description FR:
        -Cette fonction appelle la fonction "text_to_morse" pour traduire un text "value" en morse et par la suite il va
        séparer chaque lettre en uttilisant la fonction split pour renvoyer une liste contenant tout les caractères du
        text "value".
    Description EN:
        -This function calls the "text_to_morse" function to translate a text "value" into morse and then it will
        separate each letter using the split function to return a list containing all the characters of the
        text "value".

    """
    morse_code = text_to_morse(value)
    return morse_code.split()


def convert_button_time(button_time: list) -> str:
    """
    :param button_time: (list type)
    :return symbol: (str type)
    Description FR:
        -Cette fonction transforme une liste de temps en nanosecondes "button_time" sur bouton en code morse.
        -ATTENTION les temps en entrés sont en nanoseconde et les valeur risque d'énormément changer au fil des mise a
        jour.
    Description EN:
        -This function will convert a list of times from button_time to morse code.
        -ATTENTION the input times are in nanoseconds and the values risk changing enormously over the updates.

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

