#!/usr/bin/env python3
from enum import Enum
from .database import Pickle

HEROES = {}

SELECTED_HEROES = []

ACTIVE_INDEX = None


def load_heroes():
    global HEROES
    HEROES = Pickle.load(Pickle.HEROES_DB)
