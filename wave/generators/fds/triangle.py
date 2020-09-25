import random

from .fds import FDSWaveGenerator

class FDSTriangleWaveGenerator(FDSWaveGenerator):
    def __init__(self):
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def baseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a triangle 
        wave.

        Returns:
            list: Waveform values in range(64)
        """
        return [
            0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30,
            32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62,
            62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32,
            30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0
        ]
