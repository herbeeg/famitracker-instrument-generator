import random

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
        self.wave_position = 0
        self.variance = variance

        super().__init__()

    def nextPair(self):
        """
        Generate a valid pair of waveform values that
        can be included in the text export and
        used to plot on the matplotlib
        graph.

        The variance is used to judge how far we can
        stray from a standard sine wave but the
        values cannot be wrapped around from 
        64 -> 0 as this will completely
        change the wave dynamics.

        Returns:
            tuple: Pair of FDS wave values
        """
        pair_one = 0
        pair_two = 0

        wave_range_first = [
            self.wrapWaveValue(self.baseRepresentation()[self.wave_position] - self.variance),
            self.wrapWaveValue(self.baseRepresentation()[self.wave_position] + self.variance)
        ]

        wave_range_second = [
            self.wrapWaveValue(self.baseRepresentation()[self.wave_position+1] - self.variance),
            self.wrapWaveValue(self.baseRepresentation()[self.wave_position+1] + self.variance)
        ]
            
        pair_one = random.randrange(wave_range_first[0], wave_range_first[0] + 1)
        pair_two = random.randrange(wave_range_second[0], wave_range_second[1] + 1)
        """Adding one to the range to include the ceiling value."""

        self.wave_position += 2
        """Increment by two as we are returning a tuple instead of a single value."""

        return (pair_one, pair_two)

    def baseRepresentation(self):
        """
        Store a base waveform value representation
        of what FamiTracker values are used
        when a user generates a sine wave.

        Returns:
            list: Waveform values in range(64)
        """
        return [
            33, 36, 39, 42, 45, 48, 50, 53, 55, 57, 59, 60, 61, 62, 63, 63,
            63, 63, 62, 61, 60, 59, 57, 55, 53, 50, 48, 45, 42, 39, 36, 33,
            30, 27, 24, 21, 18, 15, 13, 10, 8, 6, 4, 3, 2, 1, 0, 0,
            0, 0, 1, 2, 3, 4, 6, 8, 10, 13, 15, 18, 21, 24, 27, 30
        ]

    def wrapWaveValue(self, wave_value):
        """
        If the wave value variation goes outside of
        what's supported, then we snap that
        value to the floor or ceiling.

        For example, if the next value to generate
        was between 59 and 69, then if we allowed 
        values of 59-05, then a value between 0 
        and 5 would heavily distort the 
        waveform.

        Args:
            wave_value (int): Current wave range value to validate

        Returns:
            int: Same value if within constraints, otherwise 0 or 64 dependant on passing the ceiling/floor
        """
        if 0 > wave_value:
            return 0
        elif self.wave_length <= wave_value:
            return 64
        else:
            return wave_value
