#!/usr/bin/env python3
from enum import Enum
from .database import Pickle

HEROES = {}

SELECTED_HEROES = []

ACTIVE_INDEX = None


def load_heroes():
    global HEROES
    HEROES = Pickle.load(Pickle.HEROES_DB)


def button_click(hero_name):
    global SELECTED_HEROES

    if hero_name in SELECTED_HEROES:
        SELECTED_HEROES.remove(hero_name)
    else:
        SELECTED_HEROES.append(hero_name)

    if ACTIVE_INDEX == None:
        highlight_all_relations()
    else:
        reset_highlight()
        highlight_related_heroes(ACTIVE_INDEX)
