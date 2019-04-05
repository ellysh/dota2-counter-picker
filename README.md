# Dota 2 Counter Picker 0.1 version

Dota 2 Counter Picker is an utility for choosing best combinations of heroes for "all pick" matches.

A current development state is available in the [`CHANGELOG.md`](CHANGELOG.md) file.

## Installation

You need two Python 2.7, Tkinter and pillow modules to launch the Dota 2 Counter Picker.

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

The `picker.py` script shows you which heroes are bad or good against the chosen one. Also, the script shows which heroes can be combined well.

![Picker Script](picker-window.png)

Start the `picker.py` script and click on the hero icon. The yellow color will highlight it. The red color highlights all heroes who can easily beat the selected one. We can say that the selected hero is "bad against" them. The green color means that the chosen hero is "good against" the selected ones. The blue color shows heroes which can be combined effectively with the selected hero in one team. It means that he "works well with" them.

There are three buttons with red, green and blue color at the bottom of the window. You can press each button filtering the highlighted heroes. If you press the red button, only heroes which are strong against the chosen one will be highlighted. The green and blue buttons work the same for "good against..." and "works well with..." heroes.

### Editor

The initial version of the database with heroes was prepared based on the [Dota 2 Wiki](https://dota2.gamepedia.com/Category:Counters). The `editor.py` script allows you to edit this database.

![Editor Script](editor-window.png)

Start the `editor.py` script. It looks like the `picker.py` script. Meaning of all colors is the same.

These are steps to remove the hero from the "bad against..." relations:

1. Choose the Lifestealer hero for example. The yellow color will highlight him.

2. Press the red button at the bottom of the window. You will see only heroes with "bad against..." relations for Lifestealer. Now you are in the editing mode.

3. Press the Monkey King hero. You will see that the color of his button becomes grey. This hero was removed from the "bad against..." relations for Lifestealer.

4. Finish the editing mode by pressing the red button again. Now you see all three relations of Lifestealer. Monkey King hero is not counter pick for Lifestealer anymore.

You can follow the same algorithm for adding a hero to relations. Also, you should follow the same steps for adding/removing a hero to the "good against..." and "works well with..." relations.

The `picker.py` and `editor.py` scripts use the same database. It means that you will see all your changes in the `picker.py` script. The database with heroes is stored in the `database/Database.pkl` file.

## Contacts

If you have any suggestions, bug reports or questions about usage of Dota 2 Counter Picker, please contact me via email petrsum@gmail.com.

## License

This project is distributed under the GPL v3.0 license
