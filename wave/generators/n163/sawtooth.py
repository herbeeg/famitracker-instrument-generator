from .n163 import NamcoWaveGenerator

class NamcoSawtoothWaveGenerator(NamcoWaveGenerator):
    """
    Generate a new N163 waveform that is 
    structurally similar to that of 
    a sawtooth wave, with a given
    hint of variance.

    Extends the NamcoWaveGenerator class.
    """
    def __init__(self, variance=5):
        """
        Track the position of the next waveform
        pair to generate so we know what values 
        we want to compare against the base 
        sawtooth wave representation.

        A "variance" value can be passed to give
        fewer or more constraints to the wave
        generator telling it how far it
        can deviate from a standard
        sawtooth wave shape.
        """
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def getBaseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a sawtooth 
        wave.

        This is referenced in FamiTracker as the
        'MML string'.

        Returns:
            list: Waveform values in range(16)
        """
        return [
            0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7,
            8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15
        ]
