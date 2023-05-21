import tkinter as tk
import time
import windows



class interface_graph:
    def __init__(self):
        self.root_type = tk.Tk()
        self.root_type.grid()
        self.text_intro_root = tk.Label(self.root_type, text="Select translation type").grid(row=0, column=0)
        self.button_window = tk.Button(self.root_type, text="windows", command=self.button_windows).grid(row=1, column=0)


        self.root_type.mainloop()

    def button_windows(self):
        self.root_type.destroy()
        self.set_root_mode()
        self.Type = "windows"

    def set_root_mode(self):
        self.root_mode = tk.Tk()
        self.root_mode.grid()
        self.text_intro_root_mode = tk.Label(self.root_mode, text="Select translation mode").grid(row=0, column=0)
        self.button_morse_to_alphabet_mode = tk.Button(self.root_mode, text="Morse to alphabet", command=self.morse_to_alphabet_bouton).grid(row=1, column=0)


    def morse_to_alphabet_bouton(self):
        self.root_mode.destroy()
        self.set_morse_to_alphabet()
        self.Mode = "MORSE_TO_ALPHABET"

    def set_morse_to_alphabet(self):
        self.root_trad = tk.Tk()
        self.root_trad.grid()
        self.text_intro_root_trad = tk.Label(self.root_trad, text="type in your text to be translated").grid(row=0, column=0)
        self.input_text = tk.Entry(self.root_trad).grid(row=1, column=0)
        self.button_trad = tk.Button(self.root_trad, text="trad", command=self.translated).grid(row=1, column=1)

    def getdata(self):
        text_a_tarduire = self.input_text.get()
        return text_a_tarduire

    def translated(self):
        if self.Type == "windows":
            if self.Mode == "MORSE_TO_ALPHABET":
                traducteur_type = windows.Windows()
                traducteur_type.sounds(self.getdata())


if __name__ == "__main__":
    fennetre = interface_graph()