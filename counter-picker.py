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

def load_pieces():
  global HEROES

  load_table(_HEROES_FILE, HEROES)

def reset_all_buttons():
  global BUTTONS

  for key, value in BUTTONS.iteritems():
    value[0].config(bg = _DEFAULT_COLOR)

def highlight_similarity(piece_name, index, first_color, second_color):
  global PIECES
  global _PURPLE_COLOR

  similarity_list = PIECES[piece_name][index].split('/')

  for key, value in BUTTONS.iteritems():
    check_similarity_list = PIECES[key][index].split('/')

    if key != piece_name:
      color = _DEFAULT_COLOR

      if similarity_list[0] in check_similarity_list:
        color = first_color
      elif 1 < len(similarity_list) \
           and similarity_list[1] in check_similarity_list:
        color = second_color

      if value[0].cget("bg") == _DEFAULT_COLOR:
        value[0].config(bg = color)
      elif color != _DEFAULT_COLOR:
        value[0].config(bg = _PURPLE_COLOR)

def highlight_species(piece_name):
  global _AZURE_COLOR
  global _BLUE_COLOR
  global _GREEN_COLOR
  global _YELLOW_COLOR

  highlight_similarity(piece_name, 0, _GREEN_COLOR, _YELLOW_COLOR)

  highlight_similarity(piece_name, 1, _AZURE_COLOR, _BLUE_COLOR)

def button_click(piece_name):
  global BUTTONS
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global SPECIES_DESCRIPTION_2
  global SPECIES_NUMBER_2
  global CLASS_DESCRIPTION
  global CLASS_NUMBER
  global SKILL_DESCRIPTION
  global PIECES
  global SPECIES
  global CLASSES
  global _RED_COLOR

  reset_all_buttons()

  BUTTONS[piece_name][0].config(bg = _RED_COLOR)

  highlight_species(piece_name)

  species = PIECES[piece_name][0].split('/')
  SPECIES_NUMBER_1.config(text = SPECIES[species[0]][0])
  SPECIES_DESCRIPTION_1.config(text = SPECIES[species[0]][1])

  if 1 < len(species):
    SPECIES_NUMBER_2.config(text = SPECIES[species[1]][0])
    SPECIES_DESCRIPTION_2.config(text = SPECIES[species[1]][1])
  else:
    SPECIES_NUMBER_2.config(text = "")
    SPECIES_DESCRIPTION_2.config(text = "")

  CLASS_NUMBER.config(text = CLASSES[PIECES[piece_name][1]][0])
  CLASS_DESCRIPTION.config(text = CLASSES[PIECES[piece_name][1]][1])

  SKILL_DESCRIPTION.config(text = PIECES[piece_name][3])

def add_button(window, button_click, piece, column, row):
  button = Button(window)
  button.grid(column = column, row = row)

  img = ImageTk.PhotoImage(Image.open( \
                           "images/heroes/" + piece + ".png"))

  button.config(image = img, command = lambda:button_click(piece), \
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
  global SPECIES_DESCRIPTION_1
  global SPECIES_NUMBER_1
  global SPECIES_DESCRIPTION_2
  global SPECIES_NUMBER_2
  global CLASS_DESCRIPTION
  global CLASS_NUMBER
  global SKILL_DESCRIPTION
  global _PURPLE_COLOR
  global _GREEN_COLOR
  global _YELLOW_COLOR
  global _AZURE_COLOR
  global _RED_COLOR

  window = Tk()

  window.title("Dota 2 Counter Picker " + _VERSION)

  buttons_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  buttons_frame.pack(fill = BOTH, expand = True)

  add_buttons(buttons_frame)

  info_frame = Frame(height = 2, bd = 1, relief = SUNKEN)
  info_frame.pack(fill = BOTH, expand = True)

  window.mainloop()

def main():
  load_pieces()

  make_window()

if __name__ == '__main__':
  main()
