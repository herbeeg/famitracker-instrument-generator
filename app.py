import tkinter as tk

import views.fds_view as fds
import views.main_menu as main

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.main.pack()
        self.pack()

    def loadView(self, view='menu'):
        self.clearView()

        if 'menu' == view:
            self.main = main.MainMenu(self)
            self.main.pack()

        if 'fds' == view:
            self.fds = fds.FDSView(self)
            self.fds.pack()
    
    def clearView(self):
        for widget in self.winfo_children():
            widget.destroy()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('FamiTracker Instrument Generator')
    root.geometry('480x320')

    app = App(master=root)
    app.mainloop()