import tkinter as tk
import wave.data.likeness as likeness

class LikenessDialog(tk.Toplevel):
    """
    Build the dialog window as a new
    top level element that can
    display likeness data.

    Extends the tkinter TopLevel class.
    """
    def __init__(self, master=None, data={}):
        """
        Store data for use when setting
        tkinter widget item text.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
            data (dict, optional): Passed data to display in the window. Defaults to {}.
        """
        super().__init__(master)
        self.master = master
        self.data = data

        self.createWidgets()
        self.setLikeness()

    def createWidgets(self):
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
        self.range_label.grid(row=0, column=0)

        self.range_value = tk.Label(self)
        self.range_value['text'] = ''
        self.range_value.grid(row=0, column=1)

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
