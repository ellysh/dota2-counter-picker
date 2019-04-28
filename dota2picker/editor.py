#!/usr/bin/env python3
from .view import make_window
from . import model


def main():
    model.load_heroes()

    make_window("Dota 2 Editor", True)


if __name__ == '__main__':
    main()

