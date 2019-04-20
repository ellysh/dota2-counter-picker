#!/usr/bin/env python3
from .persistence import Csv, Pickle, pickle2csv


def main():
    pickle2csv(Pickle.HEROES_DB, Csv.HEROES_DB)


if __name__ == '__main__':
    main()
