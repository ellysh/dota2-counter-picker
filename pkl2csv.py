#!/usr/bin/env python3

from csv import reader
import pickle

_VERSION = "0.5"
_CSV_FILE = "database/Database.csv"
_HEROES_FILE = "database/Database.pkl"

HEROES = {}

def load_heroes():
  global HEROES

  with open(_HEROES_FILE, "rb") as handle:
    HEROES = pickle.load(handle)

def print_header(f):
  f.write("Hero;Bad against...;Good against...;Works well with...\n")

def print_heroes(f):
  for hero in sorted(HEROES.keys()):
    f.write(hero)
    f.write(";")
    f.write(", ".join(HEROES[hero][0]))
    f.write(";")
    f.write(", ".join(HEROES[hero][1]))
    f.write(";")
    f.write(", ".join(HEROES[hero][2]))
    f.write("\n")

def save_csv():
  global HEROES

  with open(_CSV_FILE, "w") as f:
    print_header(f)

    print_heroes(f)

def main():
  load_heroes()

  save_csv()

if __name__ == '__main__':
  main()
