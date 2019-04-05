# Dota 2 Counter Picker 0.1 version

Dota 2 Counter Picker is an utility for choosing best combinations of heroes for "all pick" matches.

A current development state is available in the [`CHANGELOG.md`](CHANGELOG.md) file.

## Installation

You need two Python 2.7, Tkinter and pillow modules to launch the Dota Auto Chess Picker.

### Windows

These are steps to install Python and required modules on Windows:

1. Download the archive with Dota 2 Counter Picker and extract it:<br/>
https://github.com/ellysh/dota2-counter-picker/archive/master.zip

2. Download the Python 2.7 distribution:<br/>
https://www.python.org/downloads/release/python-2715/

3. Install Python 2.7.

4. Install the pip utility with the following command in the command line:<br/>
`python get-pip.py`

5. Install the `pillow` module:<br/>
`pip install pillow`

### Linux

These are steps to install Python and required modules on Linux:

1. Download the archive with Dota 2 Counter Picker and extract it:<br/>
https://github.com/ellysh/dota2-counter-picker/archive/master.zip

2. Install the Tkinter module:<br/>
`sudo apt-get install python-tk`

3. Install the `pillow` module:<br/>
`pip install pillow`

## Usage

### Picker

The `picker.py` script shows you which heroes are bad or good against the picked one. Also, the script shows which heroes can be combined well.

![Picker](counter-picker-window.png)

Start the `picker.py` script and click on the hero icon. The yellow color will highlight it. The red color highlights all heroes who can easily beat the selected one. The green color means that these heroes are weak against the selected one. The blue color shows which heroes can be combined effectively with the selected hero in one team.

## Contacts

If you have any suggestions, bug reports or questions about usage of Dota 2 Counter Picker, please contact me via email petrsum@gmail.com.

## License

This project is distributed under the GPL v3.0 license
