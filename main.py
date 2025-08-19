import curses
from cursesui.core import App
from cursesui.widgets import Label, Button, Frame
from cursesui.themes import DarkTheme

def main(stdscr):
    app = App(stdscr, theme=DarkTheme())

    label = Label("Welcome!", 2, 1)
    button = Button("Click Me", 2, 3, on_press=lambda: label.set_text("Clicked!"))

    frame = Frame(1, 0, 40, 10, title="Main")
    frame.add_widget(label)
    frame.add_widget(button)

    app.add_widget(frame)
    app.mainloop()

if __name__ == "__main__":
    curses.wrapper(main)
