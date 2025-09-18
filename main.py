import curses
import tkurses.core as core
import tkurses.widgets as widgits


def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  0, 0))


def main(stdscr):
    screen = stdscr
    app = core.App(screen, "themes/dark.json")
    text = widgits.TextBox((10,10),(100,9100),False)
    button = widgits.Input('button',(0,0),(10,10),on_buttonPress)
    app.add_widget(button)
    app.add_widget(text)
    app.mainloop()


curses.wrapper(main)
