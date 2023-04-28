import api


class Raspberry:
    def __init__(self):
        self.traducteur = api.MorseTrad()

    def show_morse_code(self, value: str):
        morse_code = self.traducteur.text_to_morse(value)
        morse_table = morse_code.split(" ")
        for letter in morse_table:
            for i in letter:
                if i == ".":
                    pass
                elif i == "_":
                    pass

    def get_text_to_show(self):
        pass
