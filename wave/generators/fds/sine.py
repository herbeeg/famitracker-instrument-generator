from .fds import FDSWaveGenerator

class FDSSineWaveGenerator(FDSWaveGenerator):
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
        super().__init__()

        self.wave_position = 0
        self.variance = variance

    def nextPair(self):
        pair_one = 0
        pair_two = 0

        self.wave_position += 2

        return (pair_one, pair_two)

    def baseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a sine wave.

        This is paired with graph plot values
        which are used to create the
        matplotlib figure element.

        Returns:
            list: 2D list of waveform and plot values
        """
        return [
            [
                33, 36, 39, 42, 45, 48, 50, 53, 55, 57, 59, 60, 61, 62, 63, 63,
                63, 63, 62, 61, 60, 59, 57, 55, 53, 50, 48, 45, 42, 39, 36, 33,
                30, 27, 24, 21, 18, 15, 13, 10, 8, 6, 4, 3, 2, 1, 0, 0,
                0, 0, 1, 2, 3, 4, 6, 8, 10, 13, 15, 18, 21, 24, 27, 30
            ],
            list(range(64))
        ]