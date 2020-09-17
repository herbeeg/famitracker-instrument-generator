import tkinter as tk

import main.main_menu as main

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.main.pack()
        self.pack()

    def loadView(self, view='menu'):
        if 'menu' == view:
            self.main = main.MainMenu(self)
            self.main.pack()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('FamiTracker Instrument Generator')

    app = App(master=root)
    app.mainloop()