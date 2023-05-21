import tkinter as tk
from tkinter import ttk

class new_windows():
    def __init__(self, titre, parent):
        self.titre = titre
        self.parent = parent
        self.popup = tk.Toplevel()
        self.popup.title(titre)
        self.popup.grid()
        ttk.Label(self.popup, text=self.titre).grid(column=0, row=0)
        ttk.Button(self.popup, text="MORSE_TO_TEXT").grid(column=0, row=1)
        ttk.Button(self.popup, text="TEXT_TO_MORSE").grid(column=0, row=2)




        
    
root = tk.Tk()
frm_one = ttk.Frame(root, padding=10)
frm_one.grid()
ttk.Label(frm_one, text="Hello welcome to morse TRADUCTOR!").grid(column=0, row=0)
ttk.Button(frm_one, text="windows", command=lambda: new_windows("windows", root)).grid(column=0, row=1)

ttk.Button(frm_one, text="Quit", command=root.destroy).grid(column=0, row=10)
root.mainloop()
