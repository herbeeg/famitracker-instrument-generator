import tkinter as tk

import views.fds_view as fds
import views.main_menu as main
import views.n163_view as n163

class App(tk.Frame):
    """
    Main container to provide a canvas
    for all application elements.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Initialise parent window populated with
        main menu elements and packs them
        for rendering onto the window.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.window_title = 'FamiTracker Instrument Generator'

        self.main.pack()
        self.pack()

    def loadView(self, view='menu'):
        """
        Switches out the container view based on
        what element of the application we 
        want to load.

        Args:
            view (str, optional): Container codename to load. Defaults to 'menu'.
        """
        self.clearView()

        if 'menu' == view:
            self.master.title('Menu - ' + self.window_title)
            self.main = main.MainMenu(self)
            self.main.pack()
        elif 'fds' == view:
            self.master.title('FDS - ' + self.window_title)
            self.fds = fds.FDSView(self)
            self.fds.pack()
        elif 'n163' == view:
            self.master.title('N163 - ' + self.window_title)
            self.n163 = n163.N163View(self)
            self.n163.pack()
    
    def clearView(self):
        """
        Destroy all elements in the current frame
        so that we can prepare the element to
        have a new frame loaded and packed.
        """
        for widget in self.winfo_children():
            widget.destroy()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('Menu - FamiTracker Instrument Generator')
    root.geometry('640x480')

    app = App(master=root)
    app.mainloop()
    