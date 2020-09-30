import random
import time

class FDSWaveGenerator:
    """
    Raw value generation for FDS waveforms and
    specific section construction when
    dealing with file exports.
    """
    def __init__(self):
        """
        Setting boundaries within the waveform
        that are compliant with the FDS
        expansion chip specification
        provided in FamiTracker.
        """
        self.wave_length = 64
        self.mod_length = 32

        self.wave = [[] for i in range(2)]
        """Creating an empty 2D array using list comprehension."""

        self.name = self.generate()
    
    def generate(self):
        """
        Generate a [plot][value] pair of lists that 
        can be directly inputted into the export 
        to give valid FDS waveform values, as 
        well as giving plots for our
        matplotlib graph. 

        The FDS waveform values generally come in
        pairs, observed by inspecting data from
        original soundtrack exports. This
        effectively reduces the number
        of values to 32 instead of
        64.

        Returns:
            int: Current Unix timestamp
        """
        index = 0

        while self.wave_length > index:
            self.wave[0].extend([index, index+1])
            self.wave[1].extend(self.nextPair())

            index += 2

        return int(time.time())

    def nextPair(self):
        """
        Generate a valid pair of waveform values that
        can be included in the text export and
        used to plot on the matplotlib
        graph.

        The variance is used to judge how far we can
        stray from a standard waveform but the
        values cannot be wrapped around from 
        64 -> 0 as this will completely
        change the wave dynamics.

        Returns:
            tuple: Pair of FDS wave values
        """
        pair_one = 0
        pair_two = 0

        wave_range_first = [
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position] - self.variance),
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position] + self.variance)
        ]

        wave_range_second = [
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position+1] - self.variance),
            self.wrapWaveValue(self.getBaseRepresentation()[self.wave_position+1] + self.variance)
        ]
            
        pair_one = random.randrange(wave_range_first[0], wave_range_first[1] + 1)
        pair_two = random.randrange(wave_range_second[0], wave_range_second[1] + 1)
        """Adding one to the range to include the ceiling value."""

        self.wave_position += 2
        """Increment by two as we are returning a tuple instead of a single value."""

        return (pair_one, pair_two)

    def wrapWaveValue(self, wave_value):
        """
        If the wave value variation goes outside of
        what's supported, then we snap that
        value to the floor or ceiling.

        For example, if the next value to generate
        was between 59 and 69, then if we allowed 
        values of 59-05, then a value between 0 
        and 5 would heavily distort the 
        waveform.

        Args:
            wave_value (int): Current wave range value to validate

        Returns:
            int: Same value if within constraints, otherwise 0 or 64 dependant on passing the ceiling/floor
        """
        if 0 > wave_value:
            return 0
        elif self.wave_length <= wave_value:
            return 64
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
        Format the FDS instrument modifications
        required by FamiTracker in such a
        way that is recognised by the
        importer.

        The first list item defines the FDS wave
        itself and the other items modify the
        waveform values and add any pitch
        modulation required.

        Returns:
            list: Formatted instrument mods aligned with FamiTracker importer
        """
        return [
            'INSTFDS    0     1   0   0   0 ' + '"' + self.getName() + '"',
            'FDSWAVE    0 : ' + ' '.join([str(s) if 10 <= s else ' ' + str(s) for s in self.getWave()[1]]),
            'FDSMOD     0 :  ' + '  '.join('0' for i in range(32))
        ]

    def getExpansion(self):
        """
        FamiTracker has many expansion chips available
        to the user, with the FDS expansion chip
        being fourth in the list.

        Returns:
            str: FDS expansion chip index reference
        """
        return '4'

    def getName(self):
        """
        String converted Unix timestamp for unique
        instrument identification.

        Returns:
            str: Converted Unix timestamp
        """
        return str(self.name)
