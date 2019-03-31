#!/usr/bin/env python

import os

_VERSION = "0.1"

_HTML_DIR = "html"

_BAD_LABEL = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px red;\""
_GOOD_LABEL = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px chartreuse;\""
_SYNERGY_LABEL = "div style=\"margin-bottom:5px; box-shadow:0px 0px 2px 4px skyblue;\""

_OUT_FILENAME = "Database.csv"

BAD_LIST = []
GOOD_LIST = []
SYNERGY_LIST = []

def process_file(filename):
    global _BAD_LABEL
    global _GOOD_LABEL
    global _SYNERGY_LABEL

    global BAD_LIST
    global GOOD_LIST
    global SYNERGY_LIST

    f = open(filename, "r")
    for line in f:
        if _BAD_LABEL in line:
            BAD_LIST.append(line[line.find("title=")+7:line.find("><img alt")-1])
        elif _GOOD_LABEL in line:
            GOOD_LIST.append(line[line.find("title=")+7:line.find("><img alt")-1])
        elif _SYNERGY_LABEL in line:
            SYNERGY_LIST.append(line[line.find("title=")+7:line.find("><img alt")-1])

def print_hero(hero, filename):
    global BAD_LIST
    global GOOD_LIST
    global SYNERGY_LIST

    f = open(filename, "a+")
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

    for hero_name in hero_files:
        process_file(_HTML_DIR + "/" + hero_name)

        print_hero(hero_name, _OUT_FILENAME)

if __name__ == '__main__':
  main()
