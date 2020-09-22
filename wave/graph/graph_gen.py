import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraphGenerator(tk.Frame):
    """
    A container that houses the generated graph
    Figure element, with plot data coming
    from the individual wave generator
    that requested it.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None, wave_table=[]):
        """
        Store the passed wave table data,
        which is x-axis labels and wave
        value pairs, which are used
        to generate the widget.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
            wave_table (list, optional): 2D list of wave graph plots. Defaults to [].
        """
        super().__init__(master)
        self.master = master

        self.wave_table = wave_table

        self.createWidget()

    def createWidget(self):
        """
        Using the matplotlib library and it's custom
        tkinter-friendly containers, we're able
        to generate a graph that can be 
        rendered onto our active
        window.

        Having the graph as a separate tkinter
        Frame allows us to use the pack()
        and grid() placing functions
        in the same window.
        """
        figure = Figure(figsize=(5,5), dpi=100)
        """Figure size is measured in inches."""
        graph = figure.add_subplot(111)
        """The default subplot, which creates one row, one column, with index one."""
        graph.plot(self.wave_table[0], self.wave_table[1])

        canvas = FigureCanvasTkAgg(figure, self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        