import constants

class FileGeneration:
    def __init__(self, expansion):
        self.file = ''

    def generate(self):
        self.file += self.headers()

        return self.file
        
    def headers(self):
        headers = ''

        headers += (constants.WRAPPER.START() + '\n\n')

        headers += (constants.SONG_INFORMATION.HEADER() + '\n')
        headers += (constants.SONG_INFORMATION.TITLE() + '\n')
        headers += (constants.SONG_INFORMATION.AUTHOR() + '\n')
        headers += (constants.SONG_INFORMATION.COPYRIGHT() + '\n\n')

        headers += (constants.SONG_COMMENT.HEADER() + '\n')
        headers += (constants.SONG_COMMENT.COMMENT() + '\n\n')

        return headers

    def instruments(self):
        return

    def footers(self):
        return
