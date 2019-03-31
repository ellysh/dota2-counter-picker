#!/bin/bash

OUT_DIR="html"

IFS=$'\n'

for HERO in $(cat heroes_list.txt)
do
  wget https://dota2.gamepedia.com/$HERO/Counters -O "$OUT_DIR/$HERO"
  #echo "$HERO" " - done"
done
