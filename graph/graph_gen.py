import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraphGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidget()

    def createWidget(self):
        figure = Figure(figsize=(5,5), dpi=100)
        graph = figure.add_subplot(111)
        graph.plot([1,2,3,4,5,6,7,8], [5,1,5,3,3,7,9,4])

        canvas = FigureCanvasTkAgg(figure, self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)