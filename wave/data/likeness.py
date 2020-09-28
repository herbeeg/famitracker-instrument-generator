class WaveLikeness:
    def __init__(self, base, comparison):
        self.base = base
        self.comparison = comparison
        
        self.total_diff = 0

    def showDialog(self):


    def checkLikeness(self):
        max_variance = []

        for index, wave_value in enumerate(base):
            self.total_diff += abs(wave_value, self.comparison[index])
            """Get the difference between two waveform integers."""

        return self.getLikeness(max_variance)

    def getLikeness(self, max_variance):
        return

    def getRanges(self, total_diff):
        return {
            'Identical': 0,
            'Very similar': 10,
            'Similar': 20,
            'Somewhat similar': 30,
            'Dissimilar': 40,
            'Completely dissimilar': 50
        }

    def getPercentage(self):
        return
