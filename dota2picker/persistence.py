#!/usr/bin/env python3
import pickle
from csv import reader
from pkg_resources import resource_filename


class Pickle(object):
    HEROES_DB = resource_filename('dota2picker', 'database/Database.pkl')

    @staticmethod
    def load(file):
        with open(file, "rb") as f: return pickle.load(f)

    @staticmethod
    def save(heroes, file):
        with open(file, "wb") as f: pickle.dump(heroes, f, protocol=pickle.HIGHEST_PROTOCOL)


class Csv(object):
    HEROES_DB = resource_filename('dota2picker', 'database/Database.csv')

    @staticmethod
    def load(file):
        heroes = {}
        with open(file) as csv_file:
            csv_reader = reader(csv_file, delimiter=';')
            # Skip the columns headers
            next(csv_reader)
            for line in csv_reader:
                heroes[line[0]] = [line[1].split(', '), line[2].split(', '), line[3].split(', ')]
        return heroes

    @staticmethod
    def save(heroes, file):
        with open(file, "w") as f:
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


def csv2pickle(csv_file, pickle_file):
    heroes = Csv.load(csv_file)
    Pickle.save(heroes, pickle_file)


def pickle2csv(pickl_file, csv_file):
    heroes = Pickle.load(pickl_file)
    Csv.save(heroes, csv_file)
