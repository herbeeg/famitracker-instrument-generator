import tkinter as tk
import wave.graph.graph_gen as graph

from .view import View
from functools import partial
from wave.generators.fds import random, sine, triangle, sawtooth, pulse_50, pulse_25

class FDSView(View):
    """
    Builds all of the N163 wave generation frame 
    elements and handles displaying of 
    dynamically created graphs.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Set default element padding for labels,
        dropdown items and buttons.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

    def generateWave(self):
        """
        Displays a visual graph of what the generated
        FDS wave looks like in terms of the shape,
        which can be useful when deciphering
        what kind of sound it could produce.

        As well as giving instructions to the raw wave
        generator itself, the generator object is
        passed over when dealing with text
        output.
        """
        self.graph_canvas = tk.Frame(self)

        if 'Any' == self.wave_type.get():
            self.generator = random.FDSRandomWaveGenerator()
        elif 'Sine' == self.wave_type.get():
            self.generator = sine.FDSSineWaveGenerator(self.wave_variance.get())
        elif 'Triangle' == self.wave_type.get():
            self.generator = triangle.FDSTriangleWaveGenerator(self.wave_variance.get())
        elif 'Sawtooth' == self.wave_type.get():
            self.generator = sawtooth.FDSSawtoothWaveGenerator(self.wave_variance.get())
        elif 'Pulse50' == self.wave_type.get():
            self.generator = pulse_50.FDSPulse50WaveGenerator(self.wave_variance.get())
        elif 'Pulse25' == self.wave_type.get():
            self.generator = pulse_25.FDSPulse25WaveGenerator(self.wave_variance.get())

        try:
            self.wave_table = self.generator.getWave()
            self.wave_graph = graph.GraphGenerator(master=self.graph_canvas, wave_table=self.wave_table)
            """The graph generator is generic enough to accept any length of wave 'pairs'."""

            self.graph_canvas.grid(row=5, column=0, columnspan=2)

            self.button_likeness = tk.Button(self, command=self.waveInfo)
            self.button_likeness['text'] = 'Wave information'
            self.button_likeness.grid(row=6, column=0)

            self.button_save = tk.Button(self, command=partial(self.saveWave, generator=self.generator))
            self.button_save['text'] = 'Save'
            self.button_save.grid(row=6, column=1, pady=self.frame_padding)
        except AttributeError as ex:
            """Using the common 'better to ask for forgiveness' principle."""
            tk.messagebox.showerror(title='Error Generating Wave', message='Unable to generate new FDS waveform.')
