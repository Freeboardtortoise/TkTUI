import curses
from curses import textpad

class CursesInputBox:
    def __init__(self, stdscr, y, x, width=30, prompt="Input: "):
        self.stdscr = stdscr
        self.y = y
        self.x = x
        self.width = width
        self.prompt = prompt
        self.buffer = ""
        self.cursor_pos = 0
        self.finished = False  # Flag to mark input complete

    def draw(self):
        # Draw prompt
        self.stdscr.addstr(self.y, self.x, self.prompt)

        # Draw rectangle box
        box_top = self.y + 1
        box_left = self.x
        box_bottom = box_top + 2
        box_right = box_left + self.width
        textpad.rectangle(self.stdscr, box_top, box_left, box_bottom, box_right)

        # Clear and draw text inside the box
        input_y = box_top + 1
        input_x = box_left + 1
        self.stdscr.addstr(input_y, input_x, " " * (self.width - 2))
        visible_text = self.buffer[:self.width - 2]
        self.stdscr.addstr(input_y, input_x, visible_text)

        # Move cursor if not finished
        if not self.finished:
            self.stdscr.move(input_y, input_x + self.cursor_pos)

        self.stdscr.refresh()

    def process_key(self, key):
        if self.finished:
            return True  # Already done

        if key in (10, 13):  # Enter
            self.finished = True
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
        elif 32 <= key <= 126:  # Printable ASCII
            if len(self.buffer) < self.width - 2:
                self.buffer = self.buffer[:self.cursor_pos] + chr(key) + self.buffer[self.cursor_pos:]
                self.cursor_pos += 1

        return False  # Not finished yet

    def get_value(self):
        return self.buffer

def main(stdscr):
    curses.curs_set(1)
    stdscr.clear()

    input1 = CursesInputBox(stdscr, y=2, x=4, width=30, prompt="Name:")
    input2 = CursesInputBox(stdscr, y=7, x=4, width=30, prompt="Email:")

    inputs = [input1, input2]
    current = 0

    finished_inputs = 0

    while finished_inputs < len(inputs):
        inputs[current].draw()
        key = stdscr.getch()

        done = inputs[current].process_key(key)
        if done:
            finished_inputs += 1
            current += 1
            if current >= len(inputs):
                break

    stdscr.clear()
    stdscr.addstr(2, 4, f"Name entered: {input1.get_value()}")
    stdscr.addstr(3, 4, f"Email entered: {input2.get_value()}")
    stdscr.refresh()
    stdscr.getch()
curses.wrapper(main)