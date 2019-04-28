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


def increment_score(state, index):
    scores = state.score.split(' ')
    scores[index] = str(int(scores[index]) + 1)
    state.score = ' '.join(scores)


def update_related_scores(list, relation):
    global HEROES_STATES

    for hero, state in HEROES_STATES.items():
        if hero in list:
            increment_score(state, Relations.Bad.value)


def update_scores():
    global HEROES_STATES

    for hero, state in HEROES_STATES.items():
        if state.selected:
            update_related_scores(state.bad_list, Relations.Bad.value)
            update_related_scores(state.good_list, Relations.Good.value)
            update_related_scores(state.well_list, Relations.Well.value)


def process_button_click(hero_name):
    select_hero(hero_name)

    update_scores()
