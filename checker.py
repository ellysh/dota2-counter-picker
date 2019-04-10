#!/usr/bin/env python

import pickle

_VERSION = "0.3"
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

def check_conflicts(hero, bad_list, good_list):
  for relation in bad_list:
    if relation in good_list:
      print("%s has %s in both \"bad agains\" and \"good against\" lists" \
            % (hero, relation))

def check_relations():
  global HEROES

  for hero, lists in HEROES.iteritems():
      for bad in lists[0]:
        if not hero in HEROES[bad][1]:
          HEROES[bad][1].append(hero)

      for good in lists[1]:
        if not hero in HEROES[good][0]:
          HEROES[good][0].append(hero)

      for well in lists[2]:
        if not hero in HEROES[well][2]:
          HEROES[well][2].append(hero)

      check_conflicts(hero, lists[0], lists[1])

def main():
  load_heroes()

  check_relations()

  save_heroes()

if __name__ == '__main__':
  main()
