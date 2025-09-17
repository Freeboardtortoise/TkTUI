import curses
import tkurses.core as core
import tkurses.widgets as widgits

def on_buttonPress(app, buttonWhat):
    app.add_widget(widgits.Label(f"button pressed {buttonWhat}",  10,5))
def main(stdscr):
    screen = stdscr
    app = core.App(screen, "themes/dark.json")
    app.add_widget(widgits.Label("Hello world",  0,0))
    button1 = widgits.Button("press me", 0,1, on_press=lambda: on_buttonPress(app, "press me button"))
    app.add_widget(button1)
    button2 = widgits.Button("press me too", 0, 2, on_press=lambda: on_buttonPress(app, "press Me too button"))
    app.add_widget(button2)
    input = widgits.InputBox("testing",(1,10),(10,2),on_press=lambda text: app.add_widget(widgits.Label(f"Text entered: {text}",10,7)))
    app.add_widget(input)
    app.mainloop()

curses.wrapper(main)