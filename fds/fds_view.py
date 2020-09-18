import tkinter as tk

import wave.generators.fds as fds
import graph.graph_gen as graph

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class FDSView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.createWidgets()

    def createWidgets(self):
        types = ['Any']

        self.wave_type = tk.StringVar(self.master)
        self.wave_type.set('Any')

        self.label_title = tk.Label(self)
        self.label_title['text'] = 'FDS Generator'
        self.label_title.grid(row=0, column=0)

        self.label_dropdown = tk.Label(self)
        self.label_dropdown['text'] = 'Wave type: '
        self.label_dropdown.grid(row=1, column=0)

        self.dropdown_type = tk.OptionMenu(self, self.wave_type, *types)
        self.dropdown_type.grid(row=1, column=1)

        self.button_generate = tk.Button(self, command=self.generateWave)
        self.button_generate['text'] = 'Generate'
        self.button_generate.grid(row=2, column=0)

    def generateWave(self):
        self.graph_canvas = tk.Frame(self)

        figure = Figure(figsize=(5,5), dpi=100)
        graph = figure.add_subplot(111)
        graph.plot([1,2,3,4,5,6,7,8], [5,1,5,3,3,7,9,4])

        canvas = FigureCanvasTkAgg(figure, self.graph_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        #self.wave_table = fds.FDSWaveGenerator()
        #self.wave_graph = graph.GraphGenerator(master=self.graph_canvas)

        self.graph_canvas.grid(row=3, column=0)