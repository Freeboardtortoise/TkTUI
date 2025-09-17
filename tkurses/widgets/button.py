from .base import Widget
import curses

class Button(Widget):
    def __init__(self, text: str, x: int, y: int, on_press=None):
        super().__init__(x, y, width=len(text) + 4, height=1)
        self.text = text
        self.on_press = on_press

    def render(self):
        theme = self.app.theme.get_input_theme()
        color = theme["colors"]
        if self.focused == True:
            forground = color["focused"]["forground"]
            background = color["focused"]["background"]
        else:
            forground = color["not-focused"]["forground"]
            background = color["not-focused"]["background"]
        # start and end theme
        if self.focused:
            startChar = theme["start"]["focused"]
            endChar = theme["end"]["focused"]
        else:
            startChar = theme["start"]["not-focused"]
            endChar = theme["end"]["not-focused"]
        
        # display
        display_text = f"{startChar}{self.text}{endChar}"
        self.app.stdscr.addstr(self.y, self.x, display_text, forground)

    def handle_input(self, key: int) -> bool:
        if key in (curses.KEY_ENTER, ord('\n')):
            if self.on_press:
                self.on_press()
            return True
        return False
