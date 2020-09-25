from .fds import FDSWaveGenerator

class FDSPulse25WaveGenerator(FDSWaveGenerator):
    """
    Generate a new FDS waveform that is 
    structurally similar to that of a 
    25% pulse wave, with a given 
    hint of variance.

    Extends the FDSWaveGenerator class.
    """
    def __init__(self, variance=5):
        """
        Track the position of the next waveform
        pair to generate so we know what values 
        we want to compare against the base 
        25% pulse wave representation.

        A "variance" value can be passed to give
        fewer or more constraints to the wave
        generator telling it how far it
        can deviate from a standard
        25% pulse wave shape.
        """
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def getBaseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a 25% pulse 
        wave.

        Returns:
            list: Waveform values in range(64)
        """
        return [0 for i in range(16)] + [63 for i in range(48)]
