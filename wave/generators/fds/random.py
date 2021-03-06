import random

from .fds import FDSWaveGenerator

class FDSRandomWaveGenerator(FDSWaveGenerator):
    """
    Allow the wave generator freedom
    to create a completely random
    new valid FDS waveform.

    Extends the FDSWaveGenerator class.
    """
    def __init__(self):
        """
        Call parent init function.
        """
        super().__init__()

    def nextPair(self):
        """
        Generate a valid, duplicate pair of waveform
        values to input both into our text file
        export as well as matplotlib graph.

        Returns:
            tuple: Duplicate pair of FDS wave values
        """
        double = random.randrange(64)
        return (double, double)
