#!/usr/bin/env python

import pickle

_VERSION = "0.2"
_HEROES_FILE = "database/Database.pkl"

HEROES = {}

def load_heroes():
  global HEROES

  with open(_HEROES_FILE, "rb") as handle:
    HEROES = pickle.load(handle)

def save_heroes():
  global HEROES

  with open(_HEROES_FILE, "wb") as handle:
    pickle.dump(HEROES, handle, protocol=pickle.HIGHEST_PROTOCOL)

def main():
  load_heroes()

  save_heroes()

if __name__ == '__main__':
  main()
