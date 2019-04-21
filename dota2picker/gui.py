#!/usr/bin/env python3
from enum import Enum
from .persistence import Pickle


class Color(Enum):
    Default = "#d9d9d9"
    Azure = "#5795f9"
    Green = "#66ce54"
    Yellow = "#f9ef31"
    Red = "#ff4f4f"


INDEX_COLORS = {
    0: Color.Red.value,
    1: Color.Green.value,
    2: Color.Azure.value
}


def load_heroes():
    return Pickle.load(Pickle.HEROES_DB)


def get_next_cell(column, row):
    column += 1
    if 10 < column:
        column = 0
        row += 1
    return column, row

