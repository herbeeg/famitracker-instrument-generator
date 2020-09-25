from .fds import FDSWaveGenerator

class FDSSawtoothWaveGenerator(FDSWaveGenerator):
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

        Returns:
            list: Waveform values in range(64)
        """
        return list(range(64))
