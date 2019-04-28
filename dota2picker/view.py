#!/usr/bin/env python3
from enum import Enum
from pkg_resources import resource_filename
from tkinter import Button, Label, Frame, Tk
from PIL import ImageTk, Image
from .version import VERSION
from . import model


INDEX_BUTTONS = {}

BUTTONS = {}


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


def get_next_cell(column, row):
    column += 1
    if 10 < column:
        column = 0
        row += 1
    return column, row

def add_label(window, letter, column, row):
    label = Label(window, text=letter, font=("Arial Bold", 12))
    label.grid(column=column, row=row)


def add_button(window, button_click, hero, column, row):
    button = Button(window)
    button.grid(column=column, row=row)

    resource = resource_filename('dota2picker',
        'images/heroes/{}.png'.format(hero))

    img = ImageTk.PhotoImage(Image.open(resource))

    button.config(image=img, command=lambda: button_click(hero),
                  compound="top", text="0 0 0",
                  font=("Arial Bold", 7), pady=0, padx=0)

    return button, img


def update_view():
    # TODO: Implement this function
    pass

def button_click(hero_name):
    model.process_button_click(hero_name)

    update_view()

def add_buttons(window):
    global BUTTONS

    row = 0
    column = 0

    last_letter = ''
    for key in sorted(model.HEROES.keys()):
        if key[0] != last_letter:
            last_letter = key[0]
            add_label(window, last_letter, column, row)

            column, row = get_next_cell(column, row)

        BUTTONS[key] = add_button(window, button_click, key,
                                  column, row)

        column, row = get_next_cell(column, row)


def make_window():
    global INDEX_BUTTONS

    window = Tk()
    window.title("Dota 2 Picker " + VERSION)

    buttons_frame = Frame(height=2, bd=1, relief="sunken")
    buttons_frame.pack(fill="both", expand=True)

    add_buttons(buttons_frame)

    info_frame = Frame(height=2, bd=1, relief="sunken")
    info_frame.pack(fill="both", expand=True)

    INDEX_BUTTONS[0] = Button(info_frame)
    INDEX_BUTTONS[0].grid(column=0, row=0)
    INDEX_BUTTONS[0].config(command=lambda: enable_index(0),
        compound="top", bg=Color.Red.value, width=8, height=2,
        font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    INDEX_BUTTONS[1] = Button(info_frame)
    INDEX_BUTTONS[1].grid(column=0, row=1)
    INDEX_BUTTONS[1].config(command=lambda: enable_index(1),
        compound="top", bg=Color.Green.value, width=8, height=2,
        font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    INDEX_BUTTONS[2] = Button(info_frame)
    INDEX_BUTTONS[2].grid(column=0, row=2)
    INDEX_BUTTONS[2].config(command=lambda: enable_index(2),
        compound="top", bg=Color.Azure.value, width=8, height=2,
        font=("Arial Bold", 5), pady=0, padx=0, relief="raised")

    bad_label = Label(info_frame, font=("Arial Bold", 12),
        text="Bad against...")
    bad_label.grid(column=1, row=0, sticky='W', padx=(20, 0))

    good_label = Label(info_frame, font=("Arial Bold", 12),
        text="Good against...")
    good_label.grid(column=1, row=1, sticky='W', padx=(20, 0))

    works_label = Label(info_frame, font=("Arial Bold", 12),
        text="Works well with...")
    works_label.grid(column=1, row=2, sticky='W', padx=(20, 0))

    window.bind('<Escape>', lambda event: reset_picked_heroes())

    window.mainloop()

