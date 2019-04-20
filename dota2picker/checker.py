#!/usr/bin/env python3
import sys
from .persistence import Pickle

_ADD_COMMAND = "-a"
_DELETE_COMMAND = "-d"

_USAGE = """Usage: checker.py [-a|-d|-h]
    -a - fix the inconsistent relations by adding missing heroes in the lists
    -d - fix the inconsistent relations by removing extra heroes from the lists
    -h - print help

Example:
    checker.py -a
"""

HEROES = {}
COMMAND = None


def print_usage(usage):
    sys.stderr.write(usage)
    sys.exit(1)


def load_heroes():
    global HEROES
    HEROES = Pickle.load(Pickle.HEROES_DB)


def save_heroes():
    global HEROES
    Pickle.save(HEROES, Pickle.HEROES_DB)


def check_conflicts(hero, bad_list, good_list):
    for relation in bad_list:
        if relation in good_list:
            print("%s has %s in both \"bad against\" and \"good against\" lists" \
                  % (hero, relation))


def perform_command(hero, change_list):
    global _ADD_COMMAND
    global _DELETE_COMMAND
    global COMMAND

    if COMMAND == _ADD_COMMAND:
        change_list.append(hero)
    elif COMMAND == _DELETE_COMMAND:
        change_list.remove(hero)


def check_missing_extra_relations(hero):
    global HEROES

    for bad in HEROES[hero][0]:
        if not hero in HEROES[bad][1]:
            print("%s is \"bad against\" %s but %s is not \"good against \" %s" % (hero, bad, bad, hero))
            perform_command(hero, HEROES[bad][1])

    for good in HEROES[hero][1]:
        if not hero in HEROES[good][0]:
            print("%s is \"good against\" %s but %s is not \"bad against \" %s" % (hero, good, good, hero))
            perform_command(hero, HEROES[good][0])

    for well in HEROES[hero][2]:
        if not hero in HEROES[well][2]:
            print("%s is \"works well with\" %s but not vice versa" % (hero, good))
            perform_command(hero, HEROES[well][2])


def check_relations():
    global HEROES

    for hero, lists in HEROES.items():
        check_conflicts(hero, lists[0], lists[1])
        check_missing_extra_relations(hero)


def main():
    global _ADD_COMMAND
    global _DELETE_COMMAND
    global COMMAND

    if len(sys.argv) == 2:
        if sys.argv[1] == _ADD_COMMAND or sys.argv[1] == _DELETE_COMMAND:
            COMMAND = sys.argv[1]
        else:
            print_usage(_USAGE)
    elif 2 < len(sys.argv):
        print_usage(_USAGE)

    load_heroes()
    check_relations()
    save_heroes()


if __name__ == '__main__':
    main()
