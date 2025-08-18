# simplecursesui.py
import curses
from curses import textpad

DEFAULT_THEME = {
    "frame_border": curses.A_NORMAL,
    "frame_title": curses.A_BOLD,
    "label": curses.A_NORMAL,
    "input_border": curses.A_NORMAL,
    "input_text": curses.A_NORMAL,
    "button_text": curses.A_BOLD,
    "button_focus": curses.A_REVERSE,
}


class Widget:
    def __init__(self, y, x, height=1, width=1):
        self.y = y
        self.x = x
        self.height = height
        self.width = width
        self.focused = False

    def draw(self, stdscr):
        pass

    def handle_key(self, key):
        return False

    def set_focus(self, focused):
        self.focused = focused

class Button(Widget):
    def __init__(self, y, x, text, on_click=None):
        super().__init__(y, x)
        self.text = text
        self.on_click = on_click
        self.padding = 2
        self.width = len(text) + self.padding * 2
        self.theme = DEFAULT_THEME

    def draw(self, stdscr):
        label = f"[ {self.text} ]"
        attr = self.theme["button_focus"] if self.focused else self.theme["button_text"]
        stdscr.addstr(self.y, self.x, label.center(self.width), attr)

    def handle_key(self, key):
        if key in (curses.KEY_ENTER, 10, 13):
            if self.on_click:
                self.on_click()
            return True
        return False


class InputBox(Widget):
    def __init__(self, y, x, width, label=""):
        super().__init__(y, x)
        self.label = label
        self.width = width
        self.buffer = ""
        self.cursor_pos = 0
        self.theme = DEFAULT_THEME

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, f"{self.label}", self.theme["label"])
        box_x = self.x + len(self.label) + 2
        input_y = self.y

        # Border using textpad
        textpad.rectangle(stdscr, input_y - 1, box_x - 1, input_y + 1, box_x + self.width)
        stdscr.chgat(input_y - 1, box_x - 1, self.width + 2, self.theme["input_border"])
        stdscr.chgat(input_y + 1, box_x - 1, self.width + 2, self.theme["input_border"])
        stdscr.chgat(input_y, box_x - 1, 1, self.theme["input_border"])
        stdscr.chgat(input_y, box_x + self.width, 1, self.theme["input_border"])

        # Draw text
        stdscr.addstr(input_y, box_x, " " * self.width, self.theme["input_text"])
        stdscr.addstr(input_y, box_x, self.buffer[:self.width], self.theme["input_text"])

        if self.focused:
            stdscr.move(input_y, box_x + self.cursor_pos)

    def handle_key(self, key):
        if key in (10, 13):
            return True
        elif key in (curses.KEY_BACKSPACE, 127):
            if self.cursor_pos > 0:
                self.buffer = self.buffer[:self.cursor_pos - 1] + self.buffer[self.cursor_pos:]
                self.cursor_pos -= 1
        elif key == curses.KEY_LEFT:
            if self.cursor_pos > 0:
                self.cursor_pos -= 1
        elif key == curses.KEY_RIGHT:
            if self.cursor_pos < len(self.buffer):
                self.cursor_pos += 1
        elif 32 <= key <= 126:
            if len(self.buffer) < self.width:
                self.buffer = self.buffer[:self.cursor_pos] + chr(key) + self.buffer[self.cursor_pos:]
                self.cursor_pos += 1
        return False

    def get_value(self):
        return self.buffer

    def get_value(self):
        return self.buffer

class Frame:
    def __init__(self, y, x, width, height, title=""):
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.title = title
        self.widgets = []
        self.focus_index = 0
        self.theme = DEFAULT_THEME

    def add_widget(self, widget):
        self.widgets.append(widget)
        widget.theme = self.theme

    def draw(self, stdscr):
        textpad.rectangle(stdscr, self.y, self.x, self.y + self.height, self.x + self.width)
        if self.title:
            stdscr.addstr(self.y, self.x + 2, f"[ {self.title} ]", self.theme["frame_title"])
        for widget in self.widgets:
            widget.draw(stdscr)

    def handle_key(self, key):
        if not self.widgets:
            return
        current = self.widgets[self.focus_index]
        finished = current.handle_key(key)

        if key == 9:  # Tab key
            self.focus_index = (self.focus_index + 1) % len(self.widgets)
            for i, w in enumerate(self.widgets):
                w.set_focus(i == self.focus_index)
        elif finished:
            self.focus_index = (self.focus_index + 1) % len(self.widgets)
            for i, w in enumerate(self.widgets):
                w.set_focus(i == self.focus_index)

    def focus_first(self):
        if self.widgets:
            self.focus_index = 0
            for i, w in enumerate(self.widgets):
                w.set_focus(i == self.focus_index)

class App:
    def __init__(self, stdscr, theme=None):
        self.stdscr = stdscr
        self.frames = []
        self.theme = theme or DEFAULT_THEME
        self.keybindings = {}

    def add_frame(self, frame):
        self.frames.append(frame)
        frame.focus_first()
        frame.theme = self.theme

    def bind_key(self, key, func):
        self.keybindings[key] = func

    def run(self):
        curses.curs_set(1)
        while True:
            self.stdscr.clear()
            for frame in self.frames:
                frame.draw(self.stdscr)
            self.stdscr.refresh()

            key = self.stdscr.getch()
            if key in self.keybindings:
                self.keybindings[key]()
            else:
                for frame in self.frames:
                    frame.handle_key(key)
