#!/usr/bin/env python3
from .persistence import Csv, Pickle


def main():
    heroes = Pickle.load(Pickle.HEROES_DB)
    Csv.save(heroes, Csv.HEROES_DB)

if __name__ == '__main__':
    main()
