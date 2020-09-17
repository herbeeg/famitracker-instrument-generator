import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('FamiTracker Instrument Generator')

    app = App(master=root)
    app.mainloop()