# FamiTracker Instrument Generator

FamiTracker instrument generation for N163 &amp; FDS expansion chips.

Written in Python as a desktop app, leveraging the *tkinter* library.

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

![FDS wave generation preview](/gifs/fds_wave.gif)

### Known limitations

1. **Waveform values are generated in pairs.**
> Originally, a standard was followed that is present in a lot of Pokemon soundtracks where the waveform values come along in pairs. For example, an MML string might start with `[0, 0, 32, 32, 48, 48, 32, 32]`. While this is okay for randomly generated waveforms, it created a more confusion with existing waveform variations and is more restrictive than it should be, based on what is possible within FamiTracker itself. More research is required about why the value pairs existed and whether in fact this current standard is normal within the confines of the FDS expansion chip.

2. **Can't switch to N163 wave generation.**
> Once the user selects any of the options from the main menu, there is no way to get back to the main menu to switch to another waveform for generation. This is poor from a user experience perspective and a back button should be included, instead of forcing the user to close and re-open the application from the command line.

3. **The wave likeness percentage may not be 100% accurate.**
>

4. **Limited information available about a particular waveform.**
>

## Namco N163 Wave Generation

![N163 wave generation preview](/gifs/n163_wave.gif)

### Known limitations

1. **Limited scope for wave variance.**
> Due to the fact that Namco N163 waveform values have a limited range of `0-15`, this means that the steps of variance available can be quite dramatic due to the limitations. While I think this is okay for now, I think there might be other ways of tackling variance for the N163 expansion chip specifically.

2. **Can't switch to FDS wave generation.**
> As noted in the FDS section, there is no way to go back to the menu or gracefully close the application.

Also see points `3.` and `4.` from the [FDS Wave Generation](#FDS-wave-generation) section.

## Saving Export Files

![Saving FamiTracker export preview](/gifs/save_file.gif)

![Viewing produced export](/gifs/file_details.gif)

### Known limitations

1. **No feedback to the user after export generation.**
>

2. **When a user presses cancel, a Python error is generated due to a missing filename.**
>

## Learnings

I've written a retrospective blog post about what I've learnt from tackling this new project and what I'd improve within the existing codebase and what I'll take with me going forward. You can read more here:

[https://jonherbst.dev/blog/famitracker-generator-learnings/](https://jonherbst.dev/blog/famitracker-generator-learnings/)