#!/bin/bash

#Testing interactive menu
python3 whereNow.py -i

#Testing Silent Menu
python3 whereNow.py -s Map.txt Journey.txt test

#Testing other length argc
python3 whereNow.py f s g sd sg

python3 whereNow.py -s s g s a g 3 s d g