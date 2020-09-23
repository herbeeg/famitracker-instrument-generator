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
