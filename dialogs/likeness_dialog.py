import tkinter as tk
import wave.data.likeness as likeness

class LikenessDialog(tk.Toplevel):
    def __init__(self, master=None, data={}):
        super().__init__(master)
        self.master = master
        self.data = data

        self.createWidgets()
        self.setLikeness()

    def createWidgets(self):
        self.range_label = tk.Label(self)
        self.range_label['text'] = 'Likeness: '
        self.range_label.grid(row=0, column=0)

        self.range_value = tk.Label(self)
        self.range_value['text'] = ''
        self.range_value.grid(row=0, column=1)

    def setLikeness(self):
        try:
            self.range_value['text'] = str(format(self.data['percentage'], '.2f')) + '%'
            """Include any trailing zeros in the likeness string."""
        except KeyError as ex:
            tk.messagebox.showerror(title='', message='Unable to get likness percentage value for wave.')
