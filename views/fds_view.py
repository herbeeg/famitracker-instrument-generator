import tkinter.filedialog
import tkinter as tk
import wave.graph.graph_gen as graph
import wave.file.file_gen as file_gen

from functools import partial
from wave.generators.fds import random, sine, triangle, sawtooth, pulse_50, pulse_25

class FDSView(tk.Frame):
    """
    Builds all of the FDS wave generation frame elements, 
    handles displaying of dynamically created graphs
    and file saving operations.

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

        self.frame_padding = 20

        self.createWidgets()

    def createWidgets(self):
        """
        Render all initial grid elements used
        for the graph generation.

        The graph container itself is not loaded
        until the "generate" button is clicked,
        with the command being hooked up
        to the generation function.
        """
        types = ['Any', 'Sine', 'Triangle', 'Sawtooth', 'Pulse50', 'Pulse25']
        variance_values = [str(i) for i in range(1, 11)]

        self.wave_type = tk.StringVar(self.master)
        self.wave_type.set('Any')
        """Allow tracking of tkinter option menu value."""

        self.wave_variance = tk.IntVar(self.master)
        self.wave_variance.set(5)
        """Allow user input to override the default variance."""

        self.label_title = tk.Label(self)
        self.label_title['text'] = 'FDS Generator'
        self.label_title.grid(row=0, column=0)

        self.label_type = tk.Label(self)
        self.label_type['text'] = 'Wave type: '
        self.label_type.grid(row=1, column=0)

        self.dropdown_type = tk.OptionMenu(self, self.wave_type, *types)
        self.dropdown_type.grid(row=2, column=0)

        self.label_variance = tk.Label(self)
        self.label_variance['text'] = 'Variance: '
        self.label_variance.grid(row=3, column=0)

        self.dropdown_variance = tk.OptionMenu(self, self.wave_variance, *variance_values)
        self.dropdown_variance.grid(row=4, column=0)

        self.button_generate = tk.Button(self, command=self.generateWave)
        self.button_generate['text'] = 'Generate'
        self.button_generate.grid(row=5, column=0, pady=self.frame_padding)

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

            self.graph_canvas.grid(row=6, column=0)

            self.button_likeness = tk.Button(self)
            self.button_likeness['text'] = 'Wave information'
            self.button_likeness.grid(row=7, column=0)

            self.button_save = tk.Button(self, command=partial(self.saveWave, generator=self.generator))
            self.button_save['text'] = 'Save'
            self.button_save.grid(row=8, column=0, pady=self.frame_padding)
        except AttributeError as ex:
            """Using the common 'better to ask for forgiveness' principle."""
            tk.messagebox.showerror(title='Error Generating Wave', message='Unable to generate new FDS waveform.')

    def saveWave(self, generator):
        """
        Generate a filedialog window when the 'Save'
        button is clicked and allow the user to
        specify a filename and location.

        Uses the 'w+' mode so that respective files
        are cleared before writing takes place.

        Args:
            generator (fds.FDSWaveGenerator): The current wave generator instance
        """
        filename = tk.filedialog.asksaveasfilename(title='Save FDS Wave', filetypes=[('Text Files', '*.txt')])

        try:
            with open(filename, 'w+') as text_file:
                file_contents = file_gen.FileGeneration(generator).generate()
                """Raw text file generation is handled separately."""
                text_file.write(file_contents)
                text_file.close()
        except Exception as ex:
            tk.messagebox.showerror(title='Error Saving Wave', message='Unable to save file %s' % filename)
            