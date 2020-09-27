import tkinter as tk

class LikenessDialog(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        return