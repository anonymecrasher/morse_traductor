from tkinter import *
import api
import windows


class InterfaceGraph:
    def __init__(self):
        self.root_type = Tk()
        self.root_type.grid()
        self.text_intro_root = Label(self.root_type, text="Select translation type")
        self.text_intro_root.grid(row=0, column=0)
        self.button_window = Button(self.root_type, text="Text to morse", command=self.button_windows)
        self.button_window.grid(row=1, column=0)
        self.root_type.title("Morse traductor")
        self.root_type.mainloop()

    def button_windows(self):
        self.root_type.destroy()
        self.set_root_mode()
        self.Type = "Text_to_morse"

    def set_root_mode(self):
        self.root_mode = Tk()
        self.root_mode.grid()
        self.text_intro_root_mode = Label(self.root_mode, text="Select translation mode")
        self.text_intro_root_mode.grid(row=0, column=0)
        self.button_text_mode = Button(self.root_mode, text="Mode text",
                                                    command=self.txt_mode_button)
        self.button_text_mode.grid(row=1, column=0)
        self.button_sound_mode = Button(self.root_mode, text="Mode sound", command=self.sound_mode_button)
        self.button_sound_mode.grid(row=2, column=0)
        self.root_mode.title("Morse traductor")

    def txt_mode_button(self):
        self.root_mode.destroy()
        self.set_trad_interface()
        self.Mode = "TEXT"

    def sound_mode_button(self):
        self.root_mode.destroy()
        self.set_trad_interface()
        self.Mode = "SOUND"

    def set_trad_interface(self):
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
        self.root_trad.title("Morse traductor")

    def translated(self):
        if self.Type == "Text_to_morse":
            if self.Mode == "SOUND":
                traducteur_type = windows.Windows()
                traducteur_type.sounds(str(self.valuee.get()))
            elif self.Mode == "TEXT":
                text_temp = api.text_to_morse(str(self.valuee.get()))
                texte=StringVar()
                texte.set(text_temp)
                text_translated = Label(self.root_trad, textvariable=texte)
                text_translated.grid(row=2,column=0)


if __name__ == "__main__":
    fenetre = InterfaceGraph()