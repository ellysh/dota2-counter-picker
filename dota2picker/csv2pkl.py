#!/usr/bin/env python3
from .persistence import Csv, Pickle, csv2pickle


def main():
    csv2pickle(Csv.HEROES_DB, Pickle.HEROES_DB)


if __name__ == '__main__':
  main()
