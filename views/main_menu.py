import tkinter as tk

from functools import partial

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        self.fds_open = tk.Button(self, command=partial(self.master.loadView, 'fds'))
        self.fds_open['text'] = 'FDS'
        self.fds_open.grid(row=0, column=0)

        self.n163_open = tk.Button(self)
        self.n163_open['text'] = 'N163'
        self.n163_open.grid(row=1, column=0)

        self.vrc7_open = tk.Button(self)
        self.vrc7_open['text'] = 'VRC7'
        self.vrc7_open.grid(row=2, column=0)
        