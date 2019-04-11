#!/usr/bin/env python

from csv import reader
import pickle

_VERSION = "0.4"
_CSV_FILE = "database/Database.csv"
_HEROES_FILE = "database/Database.pkl"

HEROES = {}

def load_heroes():
  global HEROES

  with open(_HEROES_FILE, "rb") as handle:
    HEROES = pickle.load(handle)

def save_csv():
  global HEROES

  with open(_CSV_FILE, "wb") as f:
    for hero in sorted(HEROES.keys()):
      f.write(hero)
      f.write(";")
      f.write(", ".join(HEROES[hero][0]))
      f.write(";")
      f.write(", ".join(HEROES[hero][1]))
      f.write(";")
      f.write(", ".join(HEROES[hero][2]))
      f.write("\n")

def main():
  load_heroes()

  save_csv()

if __name__ == '__main__':
  main()
