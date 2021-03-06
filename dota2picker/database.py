#!/usr/bin/env python3
import pickle
import os
import ntpath
import sys
from csv import reader
from pkg_resources import resource_filename
from shutil import copyfile

if sys.platform == "win32":
    USER_PATH = os.path.expanduser("~") + "/AppData/Local/dota2picker/"
else:
    USER_PATH = os.path.expanduser("~") + "/.local/share/dota2picker/"

def get_filename(resource):
    return USER_PATH + ntpath.basename(resource)

def copy_resource_file(resource):
    path = get_filename(resource)

    if os.path.exists(path): return

    if not os.path.exists(USER_PATH):
        os.mkdir(USER_PATH)

    copyfile(resource, path)

class Pickle(object):
    HEROES_DB = resource_filename('dota2picker', 'database/Database.pkl')

    @staticmethod
    def load(file):
        copy_resource_file(file)

        with open(get_filename(file), "rb") as f: return pickle.load(f)

    @staticmethod
    def save(heroes, file):
        with open(get_filename(file), "wb") as f: pickle.dump(heroes, f, protocol=pickle.HIGHEST_PROTOCOL)


class Csv(object):
    HEROES_DB = resource_filename('dota2picker', 'database/Database.csv')

    @staticmethod
    def load(file):
        copy_resource_file(file)

        heroes = {}
        with open(get_filename(file)) as csv_file:
            csv_reader = reader(csv_file, delimiter=';')
            # Skip the columns headers
            next(csv_reader)
            for line in csv_reader:
                heroes[line[0]] = [line[1].split(', '), line[2].split(', '), line[3].split(', ')]
        return heroes

    @staticmethod
    def save(heroes, file):
        with open(get_filename(file), "w") as f:
            header = "Hero;Bad against...;Good against...;Works well with...\n"
            entry = "{name};{bad_against};{good_against};{works_well}\n"
            f.write(header)
            for hero in sorted(heroes.keys()):
                f.write(entry.format(
                    name=hero,
                    bad_against=', '.join(heroes[hero][0]),
                    good_against=', '.join(heroes[hero][1]),
                    works_well=', '.join(heroes[hero][2])
                ))
