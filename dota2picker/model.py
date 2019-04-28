#!/usr/bin/env python3
from enum import Enum
from .database import Pickle

HEROES = {}

HEROES_STATES = {}


class HeroState:
    def __init__(self, hero_relations):
        self.bad_list = hero_relations[0]
        self.good_list = hero_relations[1]
        self.well_list = hero_relations[2]
        self.selected = False

        # TODO: Use score for choosing the right color for highlighting
        self.score = "0 0 0"


def heroes2states(heroes):
    global HEROES_STATES
    HEROES_STATES = {hero : HeroState(heroes[hero]) for hero in heroes.keys()}


def load_heroes():
    global HEROES
    HEROES = Pickle.load(Pickle.HEROES_DB)

    heroes2states(HEROES)


def select_hero(hero_name):
    for hero, state in HEROES_STATES.items():
        if hero == hero_name:
            state.selected = not state.selected
            break

