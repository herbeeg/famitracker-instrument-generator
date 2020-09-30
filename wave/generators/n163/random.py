import random

from .n163 import NamcoWaveGenerator

class NamcoRandomWaveGenerator(NamcoWaveGenerator):
    """
    Allow the wave generator freedom
    to create a completely random
    new valid N163 waveform.

    Extends the NamcoWaveGenerator class.
    """
    def __init__(self):
        """
        Call parent init function.
        """
        super().__init__()

    def nextNote(self):
        """
        Generate the next waveform value that can 
        be included in the text export and
        used to plot on the matplotlib
        graph.

        Returns:
            int: N163 valid note value
        """
        return random.randrange(16)
