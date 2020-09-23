from .fds import FDSWaveGenerator

class FDSPulse50WaveGenerator(FDSWaveGenerator):
    def __init__(self):
        super().__init__()

    def nextPair(self):
        """
        Generate a valid, duplicate pair of waveform
        values to input both into our text file
        export as well as matplotlib graph.
        """
        return
