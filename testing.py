# main.py
import curses
from simplecursesui import App, Frame, InputBox, Button

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA, -1)

    # Define a custom theme
    theme = {
        "frame_border": curses.A_DIM,
        "frame_title": curses.color_pair(1) | curses.A_BOLD,
        "label": curses.color_pair(1),
        "input_border": curses.A_DIM,
        "input_text": curses.A_NORMAL,
        "button_text": curses.color_pair(1),
        "button_focus": curses.color_pair(2),
    }

    def on_submit():
        stdscr.clear()
        stdscr.addstr(2, 2, f"Submitted: {name_input.get_value()}")
        stdscr.refresh()
        stdscr.getch()
        exit()

    h, w = stdscr.getmaxyx()
    frame_width = 50
    frame_height = 12

    frame = Frame(y=(h - frame_height)//2, x=(w - frame_width)//2,
                  width=frame_width, height=frame_height, title="Colorful Form")

    name_input = InputBox(y=frame.y + 3, x=frame.x + 3, width=30, label="Name:")
    email_input = InputBox(y=frame.y + 5, x=frame.x + 3, width=30, label="Email:")
    submit_button = Button(y=frame.y + 7, x=frame.x + 3, text="Submit", on_click=on_submit)

    frame.add_widget(name_input)
    frame.add_widget(email_input)
    frame.add_widget(submit_button)

    app = App(stdscr, theme=theme)
    app.add_frame(frame)

    # Add global keybinding
    app.bind_key(ord('q'), lambda: exit())
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)
