import dialogs.likeness_dialog as dialog
import tkinter.filedialog
import tkinter as tk
import wave.data.likeness as likeness
import wave.file.file_gen as file_gen

class View(tk.Frame):
    """
    Builds all of the wave generation frame elements, 
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

        self.label_type = tk.Label(self)
        self.label_type['text'] = 'Wave type: '
        self.label_type.grid(row=0, column=0, columnspan=2)

        self.dropdown_type = tk.OptionMenu(self, self.wave_type, *types)
        self.dropdown_type.grid(row=1, column=0, columnspan=2)

        self.label_variance = tk.Label(self)
        self.label_variance['text'] = 'Variance: '
        self.label_variance.grid(row=2, column=0, columnspan=2)

        self.dropdown_variance = tk.OptionMenu(self, self.wave_variance, *variance_values)
        self.dropdown_variance.grid(row=3, column=0, columnspan=2)

        self.button_generate = tk.Button(self, command=self.generateWave)
        self.button_generate['text'] = 'Generate'
        self.button_generate.grid(row=4, column=0, pady=self.frame_padding, columnspan=2)

    def saveWave(self, generator):
        """
        Generate a filedialog window when the 'Save'
        button is clicked and allow the user to
        specify a filename and location.

        Uses the 'w+' mode so that respective files
        are cleared before writing takes place.

        Args:
            generator (multi): The current wave generator instance
        """
        filename = tk.filedialog.asksaveasfilename(title='Save Wave', filetypes=[('Text Files', '*.txt')])

        try:
            with open(filename, 'w+') as text_file:
                file_contents = file_gen.FileGeneration(generator).generate()
                """Raw text file generation is handled separately."""
                text_file.write(file_contents)
                text_file.close()
        except Exception as ex:
            tk.messagebox.showerror(title='Error Saving Wave', message='Unable to save file %s' % filename)

    def waveInfo(self):
        """
        Create a new tkinter TopLevel widget with
        information about the most recently
        generated waveform.
        """
        try:
            likeness_data = {
                'percentage': likeness.WaveLikeness(base=self.generator.getBaseRepresentation(), comparison=self.generator.getWave()[1]).getLikeness()
            }

            likeness_dialog = dialog.LikenessDialog(data=likeness_data)
        except AttributeError as ex:
            tk.messagebox.showinfo(title='Cannot Retrieve Data', message='Unable to retrieve information for randomly generated waves.')
