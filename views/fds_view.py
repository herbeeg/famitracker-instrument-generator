import tkinter.filedialog
import tkinter as tk

import wave.generators.fds as fds
import wave.graph.graph_gen as graph
import wave.file.file_gen as file_gen

from functools import partial

class FDSView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 20

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
        self.dropdown_type.grid(row=2, column=0)

        self.button_generate = tk.Button(self, command=self.generateWave)
        self.button_generate['text'] = 'Generate'
        self.button_generate.grid(row=3, column=0, pady=self.frame_padding)

    def generateWave(self):
        self.graph_canvas = tk.Frame(self)

        self.generator = fds.FDSWaveGenerator()
        self.wave_table = self.generator.getWave()
        self.wave_graph = graph.GraphGenerator(master=self.graph_canvas, wave_table=self.wave_table)

        self.graph_canvas.grid(row=4, column=0)

        self.button_save = tk.Button(self, command=partial(self.saveWave, generator=self.generator))
        self.button_save['text'] = 'Save'
        self.button_save.grid(row=5, column=0, pady=self.frame_padding)

    def saveWave(self, generator):
        filename = tk.filedialog.asksaveasfilename(title='Save FDS Wave', filetypes=[('Text Files', '*.txt')])

        try:
            with open(filename, 'w+') as text_file:
                file_contents = file_gen.FileGeneration(generator).generate()
                text_file.write(file_contents)
                text_file.close()
        except Exception as ex:
            tk.messagebox.showerror(title='Error Saving Wave', message='Unable to save file %s' % filename)
            