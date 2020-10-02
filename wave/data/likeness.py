import numpy

class WaveLikeness:
    """
    Getting detailed information about a
    waveform's composition, including
    likeness to other 'structured'
    known waveforms.
    """
    def __init__(self, base, comparison, ceiling):
        """
        Both sets of waveform values
        stored for later use during
        likeness comparisons.

        Args:
            base (list):        Known waveform type values
            comparison (list):  Generated waveform type values
            ceiling (int):      Waveform value limit
        """
        self.base = base
        self.comparison = comparison
        self.ceiling = ceiling

    def getLikeness(self):
        """
        Get a likeness percentage for each
        waveform value in the list and
        take the mean.

        Returns:
            float: Mean likeness value, to 2 decimal places
        """
        percentages = []

        for index, wave_value in enumerate(self.base):
            base_diff = abs(wave_value - self.comparison[index])
            """Get the difference between two waveform integers."""

            percentages.append(self.getPercentage(index, base_diff))

        return round(numpy.mean(percentages), 2)

    def getPercentage(self, list_index, diff):
        """
        In order to calculate a 'percentage', we need
        to work out what the highest difference
        value can be for each waveform value
        in the list.

        Using this higher value, we can divide the
        actual difference value by this number
        in order to get a variance value that
        can be converted to a percentage.

        For example:
        - Base wave value: 48
        - Difference value: 6
        - Result: 6 / 48 = 0.125 
            = 12.5% variance 
            = 87.50% likeness

        Args:
            list_index (int):   Pointer to check the base wave value
            diff (int):         Current waveform value difference

        Returns:
            float: Non-rounded float percentage
        """
        bound = 0

        base_value = self.base[list_index]

        if abs(0 - base_value) < abs(self.ceiling - base_value):
            """Use whichever bound value is higher when making likeness calculations."""
            bound = abs(self.ceiling - base_value)
        else:
            bound = abs(0 - base_value)

        return (1 - (diff / bound)) * 100
        """Convert to percentage."""
