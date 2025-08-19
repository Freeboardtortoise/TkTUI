import curses
import tkurses.core as core
import tkurses.widgets as widgits
from tkurses.themes import DarkTheme

def main(stdscr):
    screen = stdscr
    app = core.App(screen, DarkTheme())
    app.add_widget(widgits.Label("Hello world",  0,0))
    app.add_widget(widgits.Button("press me", 1,0))

    screen.getch()
curses.wrapper(main)