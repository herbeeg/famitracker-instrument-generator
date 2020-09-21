import constants

class FileGeneration:
    def __init__(self, generator):
        self.file = ''
        self.expansion = generator.getExpansion()
        self.instrument_mods = generator.getInstrument()

    def generate(self):
        self.file += self.headers()
        self.file += self.information()
        self.file += self.comment()
        self.file += self.settings()
        self.file += self.macros()
        self.file += self.dpcm()
        self.file += self.instruments()

        return self.file
        
    def headers(self):
        return (constants.WRAPPER.START() + '\n\n')

    def information(self):
        output = ''
        output += (constants.SONG_INFORMATION.HEADER() + '\n')
        output += (constants.SONG_INFORMATION.TITLE() + '\n')
        output += (constants.SONG_INFORMATION.AUTHOR() + '\n')
        output += (constants.SONG_INFORMATION.COPYRIGHT() + '\n\n')

        return output

    def comment(self):
        output = ''
        output += (constants.SONG_COMMENT.HEADER() + '\n')
        output += (constants.SONG_COMMENT.COMMENT() + '\n\n')

        return output

    def settings(self):
        output = ''
        output += (constants.GLOBAL_SETTINGS.HEADER() + '\n')
        output += (constants.GLOBAL_SETTINGS.MACHINE() + '\n')
        output += (constants.GLOBAL_SETTINGS.FRAMERATE() + '\n')
        output += (constants.GLOBAL_SETTINGS.EXPANSION() + str(self.expansion) + '\n')
        output += (constants.GLOBAL_SETTINGS.VIBRATO() + '\n')
        output += (constants.GLOBAL_SETTINGS.SPLIT() + '\n\n')

        return output

    def macros(self):
        return (constants.MACROS.HEADER() + '\n\n')

    def dpcm(self):
        return (constants.DPCM_SAMPLES.HEADER() + '\n\n')

    def instruments(self):
        output = ''
        output += (constants.INSTRUMENTS.HEADER() + '\n')

        for instrument in self.instrument_mods:
            output += (instrument + '\n')

        output += '\n'

        return output

    def footers(self):
        return (constants.WRAPPER.END())
