from .n163 import NamcoWaveGenerator

class NamcoSineWaveGenerator(NamcoWaveGenerator):
    """
    Generate a new N163 waveform that is 
    structurally similar to that of 
    a sine wave, with a given
    hint of variance.

    Extends the NamcoWaveGenerator class.
    """
    def __init__(self, variance=5):
        """
        Track the position of the next waveform
        pair to generate so we know what values 
        we want to compare against the base 
        sine wave representation.

        A "variance" value can be passed to give
        fewer or more constraints to the wave
        generator telling it how far it
        can deviate from a standard
        sine wave shape.
        """
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def getBaseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a sine wave.

        Returns:
            list: Waveform values in range(16)
        """
        return [
            8, 9, 11, 12, 13, 14, 15, 15, 15, 15, 14, 14, 13, 11, 10, 9, 
            7, 6, 4, 3, 2, 1, 0, 0, 0, 0, 1, 1, 2, 4, 5, 6
        ]
