class WRAPPER:
    @staticmethod
    def START():
        return '# FamiTracker text export 0.4.2'
    
    @staticmethod
    def END():
        return '# End of export'

class SONG_INFORMATION:
    @staticmethod
    def HEADER():
        return '# Song information'
        
    @staticmethod
    def TITLE():
        return 'TITLE           ' + '"My Generated Song"'

    @staticmethod
    def AUTHOR():
        return 'AUTHOR          ' + '"Jonpon"'

    @staticmethod
    def COPYRIGHT():
        return 'COPYRIGHT       ' + '"(c) Jon Herbst"'

class SONG_COMMENT:
    @staticmethod
    def HEADER():
        return '# Song comment'

    @staticmethod
    def COMMENT():
        return 'COMMENT ' + '"A blank song with a randomly generated instrument."'

class GLOBAL_SETTINGS:
    @staticmethod
    def HEADER():
        return '# Global settings'

    @staticmethod
    def MACHINE():
        return 'MACHINE         ' + str(0)
    
    @staticmethod
    def FRAMERATE():
        return 'FRAMERATE       ' + str(0)

    @staticmethod
    def EXPANSION():
        return 'EXPANSION       '

    @staticmethod
    def VIBRATO():
        """
        'New style' vibrato.
        """
        return 'VIBRATO         ' + str(1)

    @staticmethod
    def SPLIT():
        return 'SPLIT           ' + str(32)

class MACROS:
    @staticmethod
    def HEADER():
        return '# Macros'

class DPCM_SAMPLES:
    @staticmethod
    def HEADER():
        return '# DPCM samples'

class INSTRUMENTS:
    @staticmethod
    def HEADER():
        return '# Instruments'

class TRACKS:
    @staticmethod
    def HEADER():
        return '# Tracks'

    @staticmethod
    def TRACK():
        return 'TRACK  64   6 150 "New song"'

    @staticmethod
    def COLUMNS():
        return 'COLUMNS : ' + ' '.join(['1' for i in range(6)])

    @staticmethod
    def ORDER():
        return [
            '00',
            '00',
            '00',
            '00',
            '00'
        ]