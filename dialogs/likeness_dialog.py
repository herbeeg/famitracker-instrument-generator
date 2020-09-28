import tkinter as tk
import wave.data.likeness as likeness

class LikenessDialog(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        self.range_label = tk.Label(self)
        self.range_label['text'] = 'Likeness: '
        self.range_label.grid(row=0, column=0)

        self.range_value = tk.Label(self)
        self.range_value['text'] = likeness.WaveLikeness().checkLikeness()