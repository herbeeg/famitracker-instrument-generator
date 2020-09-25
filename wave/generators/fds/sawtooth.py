from .fds import FDSWaveGenerator

class FDSSawtoothWaveGenerator(FDSWaveGenerator):
    def __init__(self, variance=5):
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def getBaseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a sawtooth 
        wave.

        Returns:
            list: Waveform values in range(64)
        """
        return list(range(64))
