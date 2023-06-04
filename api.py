MORSE_TO_ALPHABET = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
                     "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
                     "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                     "-.--": "Y", "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                     ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", ".-.-.-": '''.''',
                     '''/''': ''' '''}

ALPHABET_TO_MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                     "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                     "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                     "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
                     "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", '''.''': ".-.-.-",
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
    Convert the list of time into a symbol (morse).

    :param button_time: (list type), time in nanosecond
    :return symbol: (str type)
    """
    symbol = ""
    for i in button_time:
        # Between 0.001s and 0.6
        if 1000000 <= i < 600000000:
            symbol = symbol + "."
        # Between 0.6s and 1.3s
        elif 600000000 <= i < 1300000000:
            symbol = symbol + "-"
        # Between 1.3s and 2.6s
        elif 1300000000 <= i < 2600000000:
            symbol = symbol + " "
        # More than 2.6s
        elif 2600000000 <= i:
            symbol = symbol + " / "
        else:
            raise ValueError
    return symbol


def time_to_symbol(time: int):
    if 1000000 <= time < 600000000:
        symbol = "."
    # Between 0.6s and 1.3s
    elif 600000000 <= time < 1300000000:
        symbol = "-"
    # Between 1.3s and 2.6s
    elif 1300000000 <= time < 2600000000:
        symbol = " "
    # More than 2.6s
    elif 2600000000 <= time:
        symbol = " / "
    else:
        raise ValueError
    return symbol


def is_morse(message: str):
    for symbols in message:
        ok = False
        for expected in [".", "-", " ", "/"]:
            if symbols == expected:
                ok = True
        if ok is False:
            return False
    return True


class MorseTime:
    def __init__(self, court: float = 0.2):
        """
        Initialize the time value for . - /
        :param court: (float type)
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
    print(is_morse("--- --- .. .  ...   . a ."))

