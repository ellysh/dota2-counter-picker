#!/usr/bin/env python3
import sys
from pkg_resources import resource_filename
from .version import VERSION
from .gui import INDEX_COLORS, load_heroes, Color, get_next_cell

if sys.platform == "win32":
    from Tkinter import *
else:
    from tkinter import *
from PIL import ImageTk, Image

INDEX_BUTTONS = {}

SELECTED_HEROES = []
ACTIVE_INDEX = None

HEROES = {}
BUTTONS = {}


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


def add_label(window, letter, column, row):
    label = Label(window, text=letter, font=("Arial Bold", 12))
    label.grid(column=column, row=row)


def add_button(window, button_click, hero, column, row):
    button = Button(window)
    button.grid(column=column, row=row)

    resource = resource_filename('dota2picker', 'images/heroes/{}.png'.format(hero))
    img = ImageTk.PhotoImage(Image.open(resource))

    button.config(image=img, command=lambda: button_click(hero),
                  compound=TOP, text="0 0 0",
                  font=("Arial Bold", 7), pady=0, padx=0)

    return button, img


def add_buttons(window):
    global BUTTONS
    global HEROES

    row = 0
    column = 0

    last_letter = ''
    for key in sorted(HEROES.keys()):
        if key[0] != last_letter:
            last_letter = key[0]
            add_label(window, last_letter, column, row)

            column, row = get_next_cell(column, row)

        BUTTONS[key] = add_button(window, button_click, key, \
                                  column, row)

        column, row = get_next_cell(column, row)


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


def make_window():
    global INDEX_BUTTONS

    window = Tk()
    window.title("Dota 2 Team Picker " + VERSION)

    buttons_frame = Frame(height=2, bd=1, relief=SUNKEN)
    buttons_frame.pack(fill=BOTH, expand=True)

    add_buttons(buttons_frame)

    info_frame = Frame(height=2, bd=1, relief=SUNKEN)
    info_frame.pack(fill=BOTH, expand=True)

    INDEX_BUTTONS[0] = Button(info_frame)
    INDEX_BUTTONS[0].grid(column=0, row=0)
    INDEX_BUTTONS[0].config(command=lambda: enable_index(0),
                            compound=TOP, bg=Color.Red.value, width=8, height=2,
                            font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    INDEX_BUTTONS[1] = Button(info_frame)
    INDEX_BUTTONS[1].grid(column=0, row=1)
    INDEX_BUTTONS[1].config(command=lambda: enable_index(1),
                            compound=TOP, bg=Color.Green.value, width=8, height=2,
                            font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    INDEX_BUTTONS[2] = Button(info_frame)
    INDEX_BUTTONS[2].grid(column=0, row=2)
    INDEX_BUTTONS[2].config(command=lambda: enable_index(2),
                            compound=TOP, bg=Color.Azure.value, width=8, height=2,
                            font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    bad_label = Label(info_frame, font=("Arial Bold", 12), text="Bad against...")
    bad_label.grid(column=1, row=0, sticky=W, padx=(20, 0))

    good_label = Label(info_frame, font=("Arial Bold", 12), text="Good against...")
    good_label.grid(column=1, row=1, sticky=W, padx=(20, 0))

    works_label = Label(info_frame, font=("Arial Bold", 12), text="Works well with...")
    works_label.grid(column=1, row=2, sticky=W, padx=(20, 0))

    window.bind('<Escape>', lambda event: reset_picked_heroes())
    window.mainloop()


def main():
    global HEROES
    HEROES = load_heroes()
    make_window()


if __name__ == '__main__':
    main()
