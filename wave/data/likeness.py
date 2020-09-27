class WaveLikeness:
    def __init__(self, base, comparison, module):
        self.base = base
        self.comparison = comparison
        self.module = module

    def checkLikeness(self):
        for index, wave_value in enumerate(base):
            diff += abs(wave_value, self.comparison[index])

        return diff

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
