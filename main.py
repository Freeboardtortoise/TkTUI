import curses
import tkurses.core as core
import tkurses.widgets as widgits


def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  10, 5))


def main(stdscr):
    screen = stdscr
    app = core.App(screen, "themes/dark.json")
    text = widgits.TextBox((0,0),(50,10),True)
    app.add_widget(text)
    app.mainloop()


curses.wrapper(main)
