import random
import time

class NamcoWaveGenerator:
    """
    Raw value generation for N163 waveforms 
    and specific section construction 
    when dealing with file exports.
    """
    def __init__(self):
        """
        Setting boundaries within the waveform
        that are compliant with the N163 
        expansion chip specification
        provided in FamiTracker.
        """
        self.wave_length = 32
        self.mod_length = 16

        self.wave = [[] for i in range(2)]
        """Creating an empty 2D array using list comprehension."""

        self.name = self.generate()
    
    def generate(self):
        """
        Generate a [plot][value] pair of lists that 
        can be directly inputted into the export 
        to give valid N163 waveform values, as 
        well as giving plots for our
        matplotlib graph. 

        Returns:
            int: Current Unix timestamp
        """
        index = 0

        while self.wave_length > index:
            self.wave[0].append(index)
            self.wave[1].append(self.nextNote())

            index += 1

        return int(time.time())

    def nextNote(self):
        """
        Generate the next waveform value that can 
        be included in the text export and
        used to plot on the matplotlib
        graph.

        The variance is used to judge how far we can
        stray from a standard waveform but the
        values cannot be wrapped around from 
        32 -> 0 as this will completely
        change the wave dynamics.

        Returns:
            int: N163 valid note value
        """
        note_value = 0

        wave_range = [
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position] - self.variance),
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position] + self.variance)
        ]
            
        note_value = random.randrange(wave_range[0], wave_range[1] + 1)
        """Adding one to the range to include the ceiling value."""

        self.wave_position += 1
        """Increment by two as we are returning a tuple instead of a single value."""

        return note_value

    def wrapWaveValue(self, wave_value):
        """
        If the wave value variation goes outside of
        what's supported, then we snap that
        value to the floor or ceiling.

        For example, if the next value to generate
        was between 14 and 19, then if we allowed 
        values of 14-03, then a value between 0 
        and 3 would heavily distort the 
        waveform.

        Args:
            wave_value (int): Current wave range value to validate

        Returns:
            int: Same value if within constraints, otherwise 0 or 15 dependant on passing the ceiling/floor
        """
        if 0 > wave_value:
            return 0
        elif self.mod_length < wave_value:
            return 15
        else:
            return wave_value

    def getWave(self):
        """
        A two-dimension list that we can use to
        plot our waveform values on the
        tkinter canvas element.

        Returns:
            list: 2D list of waveform plot values
        """
        return self.wave

    def getInstrument(self):
        """
        Format the N163 instrument modifications
        required by FamiTracker in such a
        way that is recognised by the
        importer.

        The first list item defines the N163 wave
        itself and the second item modifies the
        waveform values and add any pitch
        modulation required.

        Returns:
            list: Formatted instrument mods aligned with FamiTracker importer
        """
        return [
            'INSTN163   0    -1  -1  -1  -1  -1  32  64   1 ' + '"' + self.getName() + '"',
            'N163WAVE   0   0 : ' + ' '.join([str(s) if 10 <= s else ' ' + str(s) for s in self.getWave()[1]])
        ]

    def getExpansion(self):
        """
        FamiTracker has many expansion chips available
        to the user, with the N163 expansion chip
        being defined here.

        Returns:
            str: N163 expansion chip index reference
        """
        return '16'

    def getName(self):
        """
        String converted Unix timestamp for unique
        instrument identification.

        Returns:
            str: Converted Unix timestamp
        """
        return str(self.name)
