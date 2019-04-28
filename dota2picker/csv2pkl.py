#!/usr/bin/env python3
from .persistence import Csv, Pickle


def main():
    heroes = Csv.load(Csv.HEROES_DB)
    Pickle.save(heroes, Pickle.HEROES_DB)

if __name__ == '__main__':
  main()
