import random

class FDSWaveGenerator:
    def __init__(self):
        self.wave_length = 64
        self.mod_length = 32

        self.wave = [[] for i in range(2)]
        """Creating an empty 2D array using list comprehension."""

        self.generate()
    
    def generate(self):
        index = 0

        while self.wave_length > index:
            self.wave[0].extend([index, index+1])
            self.wave[1].extend(self.nextPair())

            index += 2

    def nextPair(self):
        double = random.randrange(64)
        return (double, double)

    def getWave(self):
        return self.wave