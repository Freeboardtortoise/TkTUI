import curses
from curses import wrapper

import TSC.client as client

import TCC.input_module as input_module

def main(stdscr):
    screen = stdscr
    screen.clear()
    input_ = input_module.CursesInputManager(screen, 0,0)
    input_.get_input()
    screen.getch()

wrapper(main)