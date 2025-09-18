import curses
import tkurses.core as core
import tkurses.widgets as widgits


def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  0, 0))


def main(stdscr):
    screen = stdscr
    app = core.App(screen, "themes/dark.json")
    text = widgits.TextBox((1,1),(90,90),False)
    app.add_widget(text)
    app.mainloop()


curses.wrapper(main)
