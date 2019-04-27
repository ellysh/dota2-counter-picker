* version 0.8.0
  - Fix the bug when database changes have no effect.

* version 0.7
  - Build the package for PyPi.
  - Code refactoring.

* version 0.6
  - Adapt all script to Python 3.

* version 0.5
  - Rework the checker.py script. Now it checks the database for consistency by default and does not change anything. There are several options to fix broken heroes relations.
  - Add columns headers to the database in the CSV format.

* version 0.4
  - Add the team-picker.py script for counter picking the whole enemy team.
  - Add feature to the checker.py script for printing conflicting relations.
  - Update the database to the consistent state.

* version 0.3
  - Switch the database format to Pickle.
  - Add converter scripts csv2pkl.py and pkl2csv.py for import/export features.
  - Add the checker.py script for checking consistency of the database.
  - Fix bugs with missing heroes.

* version 0.2
  - Add the editor.py script.
  - Add filters to the parser.py script.
  - Change the database format to pickle.

* version 0.1
  - Implement basic features of the picker.
