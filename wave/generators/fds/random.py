import random

from .fds import FDSWaveGenerator

class FDSRandomWaveGenerator(FDSWaveGenerator):
    """
    Raw value generation for FDS waveforms and
    specific section construction when
    dealing with file exports.
    """
    def __init__(self):
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
        