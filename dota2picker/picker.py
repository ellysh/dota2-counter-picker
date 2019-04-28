#!/usr/bin/env python3
from .view import make_window
from . import model


def reset_all_buttons():
    global BUTTONS

    for key, value in BUTTONS.items():
        value[0].config(bg=Color.Default.value)
        value[0].config(text="0 0 0")


def reset_highlight():
    global BUTTONS
    global SELECTED_HEROES

    reset_all_buttons()

    for hero in SELECTED_HEROES:
        BUTTONS[hero][0].config(bg=Color.Yellow.value)


def increment_score(button, index):
    scores = button.cget("text").split(' ')
    scores[index] = str(int(scores[index]) + 1)
    button.config(text=' '.join(scores))


def is_score_matches_index(button, index):
    scores = button.cget("text").split(' ')
    if index == 0:
        return int(scores[1]) < int(scores[0])
    elif index == 1:
        return int(scores[0]) < int(scores[1])
    elif index == 2:
        return scores[0] == '0' and scores[1] == '0' and 0 < int(scores[2])

    return False


def highlight_related_heroes(index):
    global BUTTONS
    global HEROES
    global SELECTED_HEROES

    for hero in SELECTED_HEROES:
        related_heroes = HEROES[hero][index]

        for key, value in BUTTONS.items():
            if not key in SELECTED_HEROES and key in related_heroes:
                increment_score(value[0], index)

            if is_score_matches_index(value[0], index):
                value[0].config(bg=INDEX_COLORS[index])


def highlight_all_relations():
    global BUTTONS

    reset_highlight()
    highlight_related_heroes(2)
    highlight_related_heroes(0)
    highlight_related_heroes(1)


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


def toggle_index_button(index):
    global INDEX_BUTTONS

    for key in INDEX_BUTTONS.keys():
        if key != index:
            INDEX_BUTTONS[key].config(relief="raised")

    if INDEX_BUTTONS[index].config("relief")[-1] == "sunken":
        INDEX_BUTTONS[index].config(relief="raised")
    else:
        INDEX_BUTTONS[index].config(relief="sunken")


def enable_index(index):
    global SELECTED_HEROES
    global ACTIVE_INDEX

    if not SELECTED_HEROES:
        return

    toggle_index_button(index)
    if index == ACTIVE_INDEX:
        ACTIVE_INDEX = None
        highlight_all_relations()
        return
    else:
        ACTIVE_INDEX = index
    reset_highlight()
    highlight_related_heroes(index)


def reset_picked_heroes():
    global BUTTONS

    for key, value in BUTTONS.items():
        if BUTTONS[key][0].cget("bg") == Color.Yellow.value:
            button_click(key)


def main():
    model.load_heroes()

    make_window()


if __name__ == '__main__':
    main()
