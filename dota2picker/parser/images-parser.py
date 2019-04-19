#!/usr/bin/env python3

import os

_VERSION = "0.6"

_IMAGES_DIR = "images"

def process_file(filename):
    new_filename = filename.replace('_minimap_icon.png', '.png')
    new_filename = new_filename.replace('_', ' ')

    os.rename(filename, new_filename)

def main():
    hero_files = os.listdir(_IMAGES_DIR)

    for hero_name in hero_files:
        process_file(_IMAGES_DIR + "/" + hero_name)

if __name__ == '__main__':
  main()
