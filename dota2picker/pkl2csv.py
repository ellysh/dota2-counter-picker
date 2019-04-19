#!/usr/bin/env python3
import pickle
from pkg_resources import resource_filename


def load_heroes(file):
    with open(file, "rb") as f: return pickle.load(f)


def save_csv(file, heroes):
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


def picle2csv(heroes_file, csv_file):
    heroes = load_heroes(heroes_file)
    save_csv(csv_file, heroes)


if __name__ == '__main__':
    csv_file = resource_filename('dota2picker' 'database/Database.csv')
    heroes_file = resource_filename('dota2picker', 'database/Database.pkl')
    picle2csv(heroes_file, csv_file)
