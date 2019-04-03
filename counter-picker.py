#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.1"
_HEROES_FILE = "database/Database.csv"

_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_BLUE_COLOR = "#144593"
_GREEN_COLOR = "#66ce54"
_YELLOW_COLOR = "#f9ef31"
_PURPLE_COLOR = "#8757f9"
_RED_COLOR = "#ff4f4f"

HEROES = {}

BUTTONS = {}

def load_table(filename, table):
  with open(filename) as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    next(csv_file)

    for line in csv_reader:
        table[line[0]] = [line[1], line[2], line[3]]

def load_heroes():
  global HEROES

  load_table(_HEROES_FILE, HEROES)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_related_heroes(hero_name):
    pass

def button_click(hero_name):
  global _RED_COLOR
  global BUTTONS
  global HEROES

  reset_all_buttons()

  BUTTONS[hero_name][0].config(bg = _RED_COLOR)

def add_button(window, button_click, hero, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/heroes/" + hero + ".png"))

  button.config(image = img, command = lambda:button_click(hero), \
                compound = TOP, \
                font=("Arial Bold", 5), pady = 0, padx = 0)

  return button, img

def add_buttons(window):
  global BUTTONS
  global HEROES

  row = 0
  column = 0

  for key, _ in HEROES.iteritems():
    BUTTONS[key] = add_button(window, button_click, key, \
                              column, row)

    column += 1

    if 10 < column:
      column = 0
      row += 1

def make_window():
  global VERSION

  window = Tk()

  window.title("Dota 2 Counter Picker " + _VERSION)

  buttons_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  buttons_frame.pack(fill = BOTH, expand = True)

  add_buttons(buttons_frame)

  info_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  info_frame.pack(fill = BOTH, expand = True)

  window.mainloop()

def main():
  load_heroes()

  make_window()

if __name__ == '__main__':
  main()
