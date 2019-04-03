#!/usr/bin/env python

from Tkinter import *
from csv import reader
from PIL import ImageTk,Image

_VERSION = "0.1"
_HEROES_FILE = "database/Database.csv"

_DEFAULT_COLOR = "#d9d9d9"
_AZURE_COLOR = "#5795f9"
_GREEN_COLOR = "#66ce54"
_YELLOW_COLOR = "#f9ef31"
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
  global BUTTON

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_related_heroes(hero_name, index, color):
  global _DEFAULT_COLOR
  global BUTTON
  global HEROES

  related_heroes = HEROES[hero_name][index].split(', ')

  for key, value in BUTTONS.iteritems():
    if key != hero_name:
      if key in related_heroes \
         and value[0].cget("bg") == _DEFAULT_COLOR:
        value[0].config(bg = color)


def button_click(hero_name):
  global _RED_COLOR
  global _YELLOW_COLOR
  global _GREEN_COLOR
  global _AZURE_COLOR
  global BUTTONS
  global HEROES

  reset_all_buttons()

  BUTTONS[hero_name][0].config(bg = _YELLOW_COLOR)

  highlight_related_heroes(hero_name, 0, _RED_COLOR)

  highlight_related_heroes(hero_name, 1, _GREEN_COLOR)

  highlight_related_heroes(hero_name, 2, _AZURE_COLOR)

def add_label(window, letter, column, row):
  label = Label(window, text=letter, font=("Arial Bold", 12))
  label.grid(column = column, row = row)

def add_button(window, button_click, hero, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/heroes/" + hero + ".png"))

  button.config(image = img, command = lambda:button_click(hero), \
                compound = TOP, \
                font=("Arial Bold", 5), pady = 0, padx = 0)

  return button, img

def get_next_cell(column, row):
  column += 1

  if 10 < column:
    column = 0
    row += 1

  return column, row

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

def make_window():
  global _RED_COLOR
  global _GREEN_COLOR
  global _AZURE_COLOR
  global VERSION

  window = Tk()

  window.title("Dota 2 Counter Picker " + _VERSION)

  buttons_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  buttons_frame.pack(fill = BOTH, expand = True)

  add_buttons(buttons_frame)

  info_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  info_frame.pack(fill = BOTH, expand = True)


  color1 = Label(info_frame, bg = _RED_COLOR, width = 4, height = 1)
  color1.grid(column = 0, row = 0)

  color2 = Label(info_frame, bg = _GREEN_COLOR, width = 4, height = 1)
  color2.grid(column = 0, row = 1)

  color3 = Label(info_frame, bg = _AZURE_COLOR, width = 4, height = 1)
  color3.grid(column = 0, row = 2)


  bad_label = Label(info_frame, font=("Arial Bold", 12), \
                    text = "Bad against...")
  bad_label.grid(column = 1, row = 0, sticky = W, padx = (20, 0))

  good_label = Label(info_frame, font=("Arial Bold", 12), \
                     text = "Good against...")
  good_label.grid(column = 1, row = 1, sticky = W, padx = (20, 0))

  works_label = Label(info_frame, font=("Arial Bold", 12), \
                      text = "Works well with...")
  works_label.grid(column = 1, row = 2, sticky = W, padx = (20, 0))

  window.mainloop()

def main():
  load_heroes()

  make_window()

if __name__ == '__main__':
  main()
