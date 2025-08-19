from typing import Optional

class Widget:
    def __init__(self, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.app = None
        self.focused = False

    def set_app(self, app):
        self.app = app

    def set_focus(self, focused: bool):
        self.focused = focused

    def render(self):
        pass  # To be implemented by subclasses

    def handle_input(self, key: int) -> bool:
        return False
