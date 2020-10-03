# FamiTracker Instrument Generator

FamiTracker instrument generation for N163 &amp; FDS expansion chips.

Written in Python as a desktop app, leveraging the *tkinter*, *matplotlib* and *numpy* libraries.

Contact: [admin@jonherbst.dev](mailto:admin@jonherbst.dev)

## Requirements

- Any Debian-based Linux distribution  
- Python 3.8 or greater (if compiling from source)
- tkinter: `sudo apt-get install python3-tk` (if compiling from source)

## Running

There are currently two routes to run the code.

### If running the executable:

- Single file executable:
    - Download the latest release file named **ft_instrument_generator**
    - Open up a new terminal window and navigate to the executable's directory
    - Run the executable using `./ft_instrument_generator`

- Dist folder executable:
    - Download the latest release distribution named **ft_instrument_generator.zip**
    - Extract the contents of the compressed folder
    - Open up a new terminal window and navigate to the directory root
    - Run the executable located at `./dist/app/app`

### If compiling from source:

Clone the repository into your chosen directory and initialise the virtual environment in the root directory with `python3 -m venv /env`. Activate your newly created environment with `source ./env/bin/activate`.

To run the application, execute the main file with `python3 app.py`.

## FDS Wave Generation

Allow the user to generate valid FDS expansion chip waveforms, used by the Famicom Disk System, that can be imported into FamiTracker attached to a basic instrument. 

![FDS wave generation preview](/gifs/fds_wave.gif)

Currently supported waveforms:

- *Random*
- *Sine*
- *Triangle*
- *Sawtooth*
- *50% Pulse*
- *25% Pulse*

A variance value between `1` and `10` can be passed for all waveforms, apart from `Random`, which corresponds to the maximum value either side of the chosen waveform can be, for each point in the wave.

### Known limitations

1. **Waveform values are generated in pairs.**
> Originally, a standard was followed that is present in a lot of Pokemon soundtracks where the waveform values come along in pairs. For example, an MML string might start with `[0, 0, 32, 32, 48, 48, 32, 32]`. While this is okay for randomly generated waveforms, it created a more confusion with existing waveform variations and is more restrictive than it should be, based on what is possible within FamiTracker itself. More research is required about why the value pairs existed and whether in fact this current standard is normal within the confines of the FDS expansion chip.

2. **Can't switch to N163 wave generation.**
> Once the user selects any of the options from the main menu, there is no way to get back to the main menu to switch to another waveform for generation. This is poor from a user experience perspective and a back button should be included, instead of forcing the user to close and re-open the application from the command line.

3. **The wave likeness percentage may not be 100% accurate.**
> The current way that likeness is calculated is dividing the integer value difference of each point of the comparison waveform by the largest integer value that it can possibly be. This means that even though there might be only a difference of `1` between values along the waveform, the percentage likeness will change each time. This makes it far harder to predict an average value and write tests for expected outputs.

4. **Limited information available about a particular waveform.**
> The `Wave Information` button that appears after a waveform is generated only provides popup information about how alike the generated wave is to what it was derived from. There is much more that could be put here to give some more feedback about what was created, particularly around randomly generated waveforms. You could give rankings and percentages for the "most alike wave type" and show the user the exact integers generated to plot the graph.

## Namco N163 Wave Generation

Allow the user to generate valid Namco N163 expansion chip waveforms, used in a small amount of games for the Nintendo Famicom, that can be imported into FamiTracker attached to a basic instrument.

![N163 wave generation preview](/gifs/n163_wave.gif)

Currently supported waveforms:

- *Random*
- *Sine*
- *Triangle*
- *Sawtooth*
- *50% Pulse*
- *25% Pulse*

A variance value between `1` and `10` can be passed for all waveforms, apart from `Random`, which corresponds to the maximum value either side of the chosen waveform can be, for each point in the wave.

### Known limitations

1. **Limited scope for wave variance.**
> Due to the fact that Namco N163 waveform values have a limited range of `0-15`, this means that the steps of variance available can be quite dramatic due to the limitations. While I think this is okay for now, I think there might be other ways of tackling variance for the N163 expansion chip specifically.

2. **Can't switch to FDS wave generation.**
> As noted in the FDS section, there is no way to go back to the menu or gracefully close the application.

Also see points `3.` and `4.` from the [FDS Wave Generation](#FDS-wave-generation) section.

## Saving Export Files

Valid export files supported by the FamiTracker import function can be generated by the application to provide seamless waveform generation for use as a basis for a new project.

![Saving FamiTracker export preview](/gifs/save_file.gif)

![Viewing produced export](/gifs/file_details.gif)

### Known limitations

1. **No feedback to the user after export generation.**
> When files are saved, the user doesn't know whether the operation was successful or what to do next, apart from close the application. A solution to this could be to have a prompt appear after the operation has finished to ask the user whether they want to open the file in their recommended text editor.

2. **When a user presses cancel, a Python error is generated due to a missing filename.**
> This exception isn't caught and errors like these should be fixed before release. This will be fixed in an upcoming patch, along with more unit testing capability.

3. **Only a full FamiTracker export file can be created, making it difficult to incorporate the instrument into existing projects.**
> A nice extension to this would be to have the ability to generate valid instrument files, with the `.fti` extension but the encoding method is unknown and could not be deciphered from an existing exported instrument.

## Learnings

I've written a retrospective blog post about what I've learnt from tackling this new project and what I'd improve within the existing codebase and what I'll take with me going forward. You can read more here:

[https://jonherbst.dev/blog/famitracker-generator-learnings/](https://jonherbst.dev/blog/famitracker-generator-learnings/)