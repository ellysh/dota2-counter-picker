#!/usr/bin/env python3
from .view import make_window
from . import model


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
