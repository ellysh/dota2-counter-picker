#!/usr/bin/env python3
from enum import Enum
from .database import Pickle

HEROES = {}

HEROES_STATES = {}

class Relations(Enum):
    Bad = 0
    Good = 1
    Well = 2


class HeroState:
    def __init__(self, hero_relations):
        self.bad_list = hero_relations[Relations.Bad.value]
        self.good_list = hero_relations[Relations.Good.value]
        self.well_list = hero_relations[Relations.Well.value]
        self.is_selected = False
        self.scores = [0, 0, 0]


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
            state.is_selected = not state.is_selected

            if state.is_selected:
                return 1
            else:
                return -1

    return 0


def update_related_scores(list, relation, increment):
    global HEROES_STATES

    for hero, state in HEROES_STATES.items():
        if hero in list:
            state.scores[relation] = state.scores[relation] + increment


def update_scores(hero, increment):
    global HEROES_STATES

    update_related_scores(HEROES_STATES[hero].bad_list,
        Relations.Bad.value, increment)

    update_related_scores(HEROES_STATES[hero].good_list,
        Relations.Good.value, increment)

    update_related_scores(HEROES_STATES[hero].well_list,
        Relations.Well.value, increment)


def process_edit_click(hero_name, index):
    global HEROES
    global HEROES_STATES

    selected_hero = None

    for hero, state in HEROES_STATES.items():
        if state.is_selected:
            selected_hero = hero

    if hero_name in HEROES[selected_hero][index]:
        HEROES[selected_hero][index].remove(hero_name)
        HEROES_STATES[hero_name].scores = [0, 0, 0]
    else:
        HEROES[selected_hero][index].append(hero_name)
        HEROES_STATES[hero_name].scores[index] = 1

    Pickle.save(HEROES, Pickle.HEROES_DB)


def process_select_click(hero_name):
    increment = select_hero(hero_name)

    update_scores(hero_name, increment)
