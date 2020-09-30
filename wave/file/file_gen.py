import constants

class FileGeneration:
    """
    Handles all text file outputs for any
    type of provided waveform.

    Each 'section' should be generic enough
    that we can pass in modifications as
    and where we see fit to handle
    multiple instance types.
    """
    def __init__(self, generator):
        """
        Get all file modifications to insert
        into the text file export.

        Args:
            generator (multi): The current wave generator instance
        """
        self.file = ''
        self.expansion = generator.getExpansion()
        self.instrument_mods = generator.getInstrument()

    def generate(self):
        """
        Text file appending is split over multiple
        lines for readability and understanding
        over what is intended to be added to
        the export.

        Returns:
            str: Full file string with appropriate newline characters
        """
        self.file += self.headers()
        self.file += self.information()
        self.file += self.comment()
        self.file += self.settings()

        if '16' == self.expansion:
            """N163 exports have an additional expansion-specific section."""
            self.file += self.namco()

        self.file += self.macros()
        self.file += self.dpcm()
        self.file += self.instruments()
        self.file += self.tracks()
        self.file += self.footers()

        return self.file
        
    def headers(self):
        """
        First string to start off the new
        text file export.

        Returns:
            str: Main file header
        """
        return (constants.WRAPPER.START() + '\n\n')

    def information(self):
        """
        Values are kept generic and non-specific
        as it is intended to have file 
        generations and randomly 
        generated waves coming
        in constantly. 

        Returns:
            str: Basic generated song information
        """
        output = ''
        output += (constants.SONG_INFORMATION.HEADER() + '\n')
        output += (constants.SONG_INFORMATION.TITLE() + '\n')
        output += (constants.SONG_INFORMATION.AUTHOR() + '\n')
        output += (constants.SONG_INFORMATION.COPYRIGHT() + '\n\n')

        return output

    def comment(self):
        """
        Generic comment values to maintain
        alignment with entire file
        generation.

        Returns:
            str: Basic generated song comments
        """
        output = ''
        output += (constants.SONG_COMMENT.HEADER() + '\n')
        output += (constants.SONG_COMMENT.COMMENT() + '\n\n')

        return output

    def settings(self):
        """
        The expansion chip passed tells FamiTracker
        what module we are working with in the
        current project. For example:

        - '4' means we are using the FDS expansion chip

        Returns:
            str: Basic generated global settings
        """
        output = ''
        output += (constants.GLOBAL_SETTINGS.HEADER() + '\n')
        output += (constants.GLOBAL_SETTINGS.MACHINE() + '\n')
        output += (constants.GLOBAL_SETTINGS.FRAMERATE() + '\n')
        output += (constants.GLOBAL_SETTINGS.EXPANSION() + str(self.expansion) + '\n')
        output += (constants.GLOBAL_SETTINGS.VIBRATO() + '\n')
        output += (constants.GLOBAL_SETTINGS.SPLIT() + '\n\n')

        return output

    def namco(self):
        """
        Namco N163 expansion chip files have an
        additional specific section telling
        FamiTracker how many channels we
        want to use in the project.

        Returns:
            str: Additional N163 global settings
        """
        output = ''
        output += (constants.NAMCO_GLOBALS.HEADER() + '\n')
        output += (constants.NAMCO_GLOBALS.N163CHANNELS() + '\n\n')
        return output

    def macros(self):
        """
        Macros are not added when a new blank
        file is created in FamiTracker so
        we don't need to populate this
        section any further.

        Returns:
            str: Basic generated macros
        """
        return (constants.MACROS.HEADER() + '\n\n')

    def dpcm(self):
        """
        DPCM, or 'Differential pulse-code modulation'
        is not required when dealing with new file 
        generation as we don't need to add any 
        created samples to the track.

        Returns:
            str: Basic generated DPCM samples
        """
        return (constants.DPCM_SAMPLES.HEADER() + '\n\n')

    def instruments(self):
        """
        Based on the expansion chip we've chosen, we
        want to display the correct intrument
        modifiers to tell FamiTracker what
        waveforms we are dealing with.

        The generator passed in has setters and
        getters so that we can keep this file
        generator class clean of any 
        potential coupling.

        Returns:
            str: Custom generated instruments section
        """
        output = ''
        output += (constants.INSTRUMENTS.HEADER() + '\n')

        for instrument in self.instrument_mods:
            output += (instrument + '\n')

        output += '\n'

        return output

    def tracks(self):
        """
        We are able to define the export file with
        no track information as newly created
        files in FamiTracker do not have
        any information attached at
        the beginning.

        We could add any base notes and modifiers
        here if we wanted to create example
        songs for an out of the box
        testing solution.

        Returns:
            str: Basic generated tracks section
        """
        output = ''
        output += (constants.TRACKS.HEADER() + '\n\n')
        output += (constants.TRACKS.TRACK() + '\n')
        output += (constants.TRACKS.COLUMNS() + '\n\n')
        output += (constants.TRACKS.ORDER() + '\n\n')

        return output

    def footers(self):
        """
        Final string to end the new text 
        file export.

        Returns:
            str: Main file footer
        """
        return (constants.WRAPPER.END())
        