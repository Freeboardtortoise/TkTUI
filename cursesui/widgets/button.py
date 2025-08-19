from .base import Widget
import curses

class Button(Widget):
    def __init__(self, text: str, x: int, y: int, on_press=None):
        super().__init__(x, y, width=len(text) + 4, height=1)
        self.text = text
        self.on_press = on_press

    def render(self):
        color = self.app.theme.get_color("primary" if self.focused else "secondary")
        display_text = f"[ {self.text} ]"
        self.app.stdscr.addstr(self.y, self.x, display_text, color)

    def handle_input(self, key: int) -> bool:
        if key in (curses.KEY_ENTER, ord('\n')):
            if self.on_press:
                self.on_press()
            return True
        return False
