import numpy

class WaveLikeness:
    def __init__(self, base, comparison):
        self.base = base
        self.comparison = comparison

    def getLikeness(self):
        diff_values = []
        percentages = []

        for index, wave_value in enumerate(self.base):
            base_diff = abs(wave_value - self.comparison[index])
            diff_values.append(base_diff)
            """Get the difference between two waveform integers."""

            percentages.append(self.getPercentage(index, base_diff))

        return round(numpy.mean(percentages), 2)

    def getRanges(self, total_diff):
        return {
            'Identical': 0,
            'Very similar': 10,
            'Similar': 20,
            'Somewhat similar': 30,
            'Dissimilar': 40,
            'Completely dissimilar': 50
        }

    def getPercentage(self, list_index, diff):
        bound = 0

        base_value = self.base[list_index]
        comparison_value = self.comparison[list_index]

        if abs(0 - base_value) < abs(64 - base_value):
            """Use whichever bound value is higher when making likeness calculations."""
            bound = abs(64 - base_value)
        else:
            bound = abs(0 - base_value)

        return (1 - (diff / bound)) * 100
        """Convert to percentage."""
