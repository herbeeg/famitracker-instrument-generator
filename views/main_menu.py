import tkinter as tk

from functools import partial

class MainMenu(tk.Frame):
    """
    Builds all of the main menu elements in
    the application which can be used by
    the parent window for rendering.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Render out the menu widgets on 
        initialisation.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        """
        Render all menu button elements and map their
        commands to the main application's view
        loader function.
        """
        self.fds_open = tk.Button(self, command=partial(self.master.loadView, 'fds'))
        self.fds_open['text'] = 'FDS'
        self.fds_open.grid(row=0, column=0)

        self.n163_open = tk.Button(self, command=partial(self.master.loadView, 'n163'))
        self.n163_open['text'] = 'N163'
        self.n163_open.grid(row=1, column=0)
