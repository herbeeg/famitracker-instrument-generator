import tkinter as tk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GraphGenerator(tk.Frame):
    def __init__(self, master=None, wave_table=[]):
        super().__init__(master)
        self.master = master

        self.wave_table = wave_table

        self.createWidget()

    def createWidget(self):
        figure = Figure(figsize=(5,5), dpi=100)
        graph = figure.add_subplot(111)
        graph.plot(self.wave_table[1], self.wave_table[0])

        canvas = FigureCanvasTkAgg(figure, self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)