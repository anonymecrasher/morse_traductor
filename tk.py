from tkinter import *
import time
import windows


class InterfaceGraph:
    def __init__(self):
        self.root_type = Tk()
        self.root_type.grid()
        self.text_intro_root = Label(self.root_type, text="Select translation type")
        self.text_intro_root.grid(row=0, column=0)
        self.button_window = Button(self.root_type, text="windows", command=self.button_windows)
        self.button_window.grid(row=1, column=0)

        self.root_type.mainloop()

    def button_windows(self):
        self.root_type.destroy()
        self.set_root_mode()
        self.Type = "windows"

    def set_root_mode(self):
        self.root_mode = Tk()
        self.root_mode.grid()
        self.text_intro_root_mode = Label(self.root_mode, text="Select translation mode")
        self.text_intro_root_mode.grid(row=0, column=0)
        self.button_morse_to_alphabet_mode = Button(self.root_mode, text="Morse to alphabet", command=self.morse_to_alphabet_button)
        self.button_morse_to_alphabet_mode.grid(row=1, column=0)

    def morse_to_alphabet_button(self):
        self.root_mode.destroy()
        self.set_morse_to_alphabet()
        self.Mode = "MORSE_TO_ALPHABET"

    def set_morse_to_alphabet(self):
        self.root_trad = Tk()
        self.root_trad.grid()
        self.text_intro_root_trad = Label(self.root_trad, text="Type in your text to be translated")
        self.text_intro_root_trad.grid(row=0, column=0)
        self.valuee = StringVar()
        self.valuee.set("Value")
        self.input_text = Entry(self.root_trad, textvariable=self.valuee)
        self.input_text.grid(row=1, column=0)
        self.button_trad = Button(self.root_trad, text="Translate", command=self.translated)
        self.button_trad.grid(row=1, column=1)

    def translated(self):
        if self.Type == "windows":
            if self.Mode == "MORSE_TO_ALPHABET":
                traducteur_type = windows.Windows()
                traducteur_type.sounds(str(self.valuee.get()))


if __name__ == "__main__":
    fenetre = InterfaceGraph()