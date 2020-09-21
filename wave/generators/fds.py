import random
import time

class FDSWaveGenerator:
    def __init__(self):
        self.wave_length = 64
        self.mod_length = 32

        self.wave = [[] for i in range(2)]
        """Creating an empty 2D array using list comprehension."""

        self.name = self.generate()
    
    def generate(self):
        index = 0

        while self.wave_length > index:
            self.wave[0].extend([index, index+1])
            self.wave[1].extend(self.nextPair())

            index += 2

        return int(time.time())

    def nextPair(self):
        double = random.randrange(64)
        return (double, double)

    def getWave(self):
        return self.wave

    def getInstrument(self):
        return [
            'INSTFDS    0     1   0   0   0 ' + '"' + self.getName() + '"',
            'FDSWAVE    0 : ' + ' '.join([str(s) if 10 <= s else ' ' + str(s) for s in self.getWave()[1]]),
            'FDSMOD     0 :  ' + '  '.join('0' for i in range(32))
        ]

    def getExpansion(self):
        return '4'

    def getName(self):
        return str(self.name)