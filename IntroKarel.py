#!/usr/bin/env python3

"""
CS106AP PyCharm Intro Project
"""

from karel.stanfordkarel import *
import platform


def draw_side():
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_left()


def draw_sqaure():
    draw_side()
    draw_side()
    draw_side()
    draw_side()


def main():
    draw_sqaure()


if __name__ == "__main__":
    if platform.python_version() != "3.7.3":
        print(
            "ERROR: You are not using the latest version of python3! You are using version: " + platform.python_version())
        print("Please follow the instructions on the CS106AP website to download python version 3.7.3")
    else:
        print("Hello, it's me, Karel! You're done with the PyCharm setup process! "
            "Now press the run button to see me draw a square. ")
        execute_karel_task(main)