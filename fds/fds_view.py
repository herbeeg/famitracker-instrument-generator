import tkinter as tk

import wave.generators.fds as fds

class FDSView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        types = ['Any']

        self.wave_type = tk.StringVar(self.master)
        self.wave_type.set('Any')

        self.label_title = tk.Label(self)
        self.label_title['text'] = 'FDS Generator'
        self.label_title.grid(row=0, column=0)

        self.label_dropdown = tk.Label(self)
        self.label_dropdown['text'] = 'Wave type: '
        self.label_dropdown.grid(row=1, column=0)

        self.dropdown_type = tk.OptionMenu(self, self.wave_type, *types)
        self.dropdown_type.grid(row=1, column=1)

        self.button_generate = tk.Button(self, command=self.generateWave)
        self.button_generate['text'] = 'Generate'
        self.button_generate.grid(row=2, column=0)

    def generateWave(self):
        self.wave_table = fds()