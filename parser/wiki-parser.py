#!/usr/bin/env python3

import os

_VERSION = "0.6"

_HTML_DIR = "html"

_BAD_LABEL = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px red;\""
_GOOD_LABEL_1 = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px chartreuse;\""
_GOOD_LABEL_2 = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px green;\""
_SYNERGY_LABEL = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px skyblue;\""

_OUT_FILENAME = "../database/Database.csv"

BAD_LIST = []
GOOD_LIST = []
SYNERGY_LIST = []

def get_hero_name(line):
  hero = line[line.find("title=")+7:line.find("><img alt")-1]

  if "Nature" in hero:
    return "Natures Prophet"

  return hero

def process_file(filename):
  global _BAD_LABEL
  global _GOOD_LABEL
  global _SYNERGY_LABEL

  global BAD_LIST
  global GOOD_LIST
  global SYNERGY_LIST

  BAD_LIST = []
  GOOD_LIST = []
  SYNERGY_LIST = []

  f = open(filename, "r")
  for line in f:
    if _BAD_LABEL in line:
      BAD_LIST.append(get_hero_name(line))
    elif _GOOD_LABEL_1 in line or _GOOD_LABEL_2 in line:
      GOOD_LIST.append(get_hero_name(line))
    elif _SYNERGY_LABEL in line:
      SYNERGY_LIST.append(get_hero_name(line))

def print_header(f):
  f.write("Hero;Bad against...;Good against...;Works well with...\n")

def print_hero(hero, f):
  global BAD_LIST
  global GOOD_LIST
  global SYNERGY_LIST

  # Fix the apostrophe sign in the hero name
  if "Nature" in hero:
    hero = "Natures Prophet"

  f.write(hero)
  f.write(";")
  f.write(", ".join(BAD_LIST))
  f.write(";")
  f.write(", ".join(GOOD_LIST))
  f.write(";")
  f.write(", ".join(SYNERGY_LIST))
  f.write("\n")

def main():
  if os.path.isfile(_OUT_FILENAME):
    os.remove(_OUT_FILENAME)

  hero_files = os.listdir(_HTML_DIR)

  with open(_OUT_FILENAME, "a+") as f:
    print_header(f)

    for hero_name in sorted(hero_files):
      process_file(_HTML_DIR + "/" + hero_name)

      print_hero(hero_name, f)

if __name__ == '__main__':
  main()
