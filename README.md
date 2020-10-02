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

## Namco N163 Wave Generation

![N163 wave generation preview](/gifs/n163_wave.gif)

## Saving Export Files

![Saving FamiTracker export preview](/gifs/save_file.gif)

![Viewing produced export](/gifs/file_details.gif)