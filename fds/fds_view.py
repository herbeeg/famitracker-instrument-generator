import tkinter as tk

class FDSView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        self.label_title = tk.Label(self)
        self.label_title['text'] = 'FDS Generator'
        self.label_title.grid(row=0, column=0)