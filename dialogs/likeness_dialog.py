import tkinter.simpledialog
import tkinter as tk
import wave.data.likeness as likeness

class LikenessDialog(tk.simpledialog.Dialog):
    """
    Build the dialog window as a new
    top level element that can
    display likeness data.

    Extends the tkinter simpledialog.Dialog class.
    """
    def __init__(self, master=None, data={}):
        """
        Store data for use when setting
        tkinter widget item text.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
            data (dict, optional): Passed data to display in the window. Defaults to {}.
        """
        self.master = master
        self.data = data
        super().__init__(master)

    def body(self, master=None):
        """
        Render likeness data widgets for the
        entire dialog window.

        The values strings are left blank as
        these will be updated separately
        after the initial widgets have
        been drawn on the grid.
        """
        self.range_label = tk.Label(self)
        self.range_label['text'] = 'Likeness: '
        self.range_label.pack()

        self.range_value = tk.Label(self)
        self.range_value['text'] = ''
        self.range_value.pack()

        self.setLikeness()

        return

    def buttonbox(self):
        box = tk.Frame(self)

        w = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        w.pack(padx=5, pady=5)

        self.bind("<Return>", self.ok)

        box.pack()

    def setLikeness(self):
        """
        Attempt to access any likeness data
        passed through the initialisation
        phase and draw that on the
        window grid.
        """
        try:
            self.range_value['text'] = str(format(self.data['percentage'], '.2f')) + '%'
            """Include any trailing zeros in the likeness string."""
        except KeyError as ex:
            tk.messagebox.showerror(title='', message='Unable to get likness percentage value for wave.')
