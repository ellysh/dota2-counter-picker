#!/usr/bin/env python

from csv import reader
import pickle

_VERSION = "0.4"
_HEROES_FILE = "database/Database.csv"
_PICKLE_FILE = "database/Database.pkl"

HEROES = {}

def load_table(filename, table):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')

    # Skip the columns headers
    csv_reader.next()

    for line in csv_reader:
        table[line[0]] = [line[1].split(', '), line[2].split(', '), line[3].split(', ')]

def load_heroes():
  global HEROES

  load_table(_HEROES_FILE, HEROES)

def save_pickle():
  global HEROES

  with open(_PICKLE_FILE, "wb") as handle:
    pickle.dump(HEROES, handle, protocol=pickle.HIGHEST_PROTOCOL)

def main():
  load_heroes()

  save_pickle()

if __name__ == '__main__':
  main()
