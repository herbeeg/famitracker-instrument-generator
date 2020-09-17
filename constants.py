class WRAPPER:
    @staticmethod
    def START():
        return '# FamiTracker text export 0.4.2'
    
    @staticmethod
    def END():
        return '# End of export'

class SONG_INFORMATION:
    @staticmethod
    def TITLE():
        return 'My Generated Song'

    @staticmethod
    def AUTHOR():
        return 'Jonpon'

    @staticmethod
    def COPYRIGHT():
        return '(c) Jon Herbst'

class SONG_COMMENT:
    @staticmethod
    def COMMENT():
        return 'A blank song with a randomly generated instrument.'

class GLOBAL_SETTINGS:
    @staticmethod
    def MACHINE():
        return 0
    
    @staticmethod
    def FRAMERATE():
        return 0

    @staticmethod
    def VIBRATO():
        """
        'New style' vibrato.
        """
        return 1

    @staticmethod
    def SPLIT():
        return 32

class TRACKS:
    @staticmethod
    def TRACK():
        return [
            64,
            6,
            150,
            'New song'
        ]

    @staticmethod
    def COLUMNS():
        return [
            1,
            1,
            1,
            1,
            1
        ]

    @staticmethod
    def ORDER():
        return [
            '00',
            '00',
            '00',
            '00',
            '00'
        ]

    @staticmethod
    def PATTERN():
        return ' : ... .. . ...'