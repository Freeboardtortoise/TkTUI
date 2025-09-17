import curses
import tkurses.core as core
import tkurses.widgets as widgits
from tkurses.themes import DarkTheme

def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  10,5))
def main(stdscr):
    screen = stdscr
    app = core.App(screen, DarkTheme())
    app.add_widget(widgits.Label("Hello world",  0,0))
    button1 = widgits.Button("press me", 0,1, on_press=lambda: on_buttonPress(app, "press me button"))
    app.add_widget(button1)
    button2 = widgits.Button("press me too", 0, 2, on_press=lambda: on_buttonPress(app, "press Me too button"))
    app.add_widget(button2)
    input = widgits.InputBox(10,10,20,10)

    while True:
        key = screen.getch()

        if button1.handle_input(key) == False:
            button2.handle_input(key)

curses.wrapper(main)