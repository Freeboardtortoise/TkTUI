import curses
import tkurses.core as core
from tkurses.widgets import Frame, Inputbox, Label
from tkurses.themes import DarkTheme

def main(stdscr):
    screen = stdscr
    app = core.app(screen, DarkTheme)
    app.add_widget(Label(text="Hello world",  0,0))