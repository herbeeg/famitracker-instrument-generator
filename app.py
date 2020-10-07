import tkinter as tk

import views.fds_view as fds
import views.main_menu as main
import views.n163_view as n163

from functools import partial

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
            self.detachBackButton()
        elif 'fds' == view:
            self.master.title('FDS - ' + self.window_title)

            self.fds = fds.FDSView(self)
            self.fds.pack()
            self.attachBackButton()
        elif 'n163' == view:
            self.master.title('N163 - ' + self.window_title)

            self.n163 = n163.N163View(self)
            self.n163.pack()
            self.attachBackButton()
    
    def clearView(self):
        """
        Destroy all elements in the current frame
        so that we can prepare the element to
        have a new frame loaded and packed.
        """
        for widget in self.winfo_children():
            widget.destroy()

    def attachBackButton(self):
        """
        Create a new, absolutely positioned back button
        element to the root frame and anchor it to
        the top-left of the window.
        """
        self.menu_back = tk.Button(self.master, padx=10, pady=5, command=partial(self.loadView, 'menu'))
        self.menu_back['text'] = '<-- Back'
        self.menu_back.pack()
        self.menu_back.place(anchor='nw', x=10)

    def detachBackButton(self):
        """
        As the back button is attached to the root
        frame, the element will be destroyed
        and re-created when necessary.
        """
        if hasattr(self, 'menu_back') and None != self.menu_back:
            self.menu_back.destroy()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('Menu - FamiTracker Instrument Generator')
    root.geometry('640x480')

    app = App(master=root)
    app.mainloop()
