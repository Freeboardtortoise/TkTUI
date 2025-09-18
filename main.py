import curses
import tkurses.core as core
import tkurses.widgets as widgits


def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  1, 1))


def main(stdscr):
    screen = stdscr
    app = core.App(screen, "themes/dark.json")
    button1 = widgits.Button("press start", 0,0,on_press= lambda: on_buttonPress(app,"tortoise"))
    input_box = widgits.Input("testing",(50,50),(10,10),on_press=lambda: app.add_widget(widgits.Label("tortoise",0,10)))
    app.add_widget(input_box)
    app.add_widget(button1)
    app.mainloop()


curses.wrapper(main)