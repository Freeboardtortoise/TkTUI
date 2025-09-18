from typing import Optional
import os

class Widget:
    def __init__(self, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None):
        terminalSize = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        print(terminalSize)
        self.x = x
        # set percentagses
        self.x = self.x/100
        self.x = int(terminalSize[0]*self.x)

        self.y = y
        # set percentage
        self.y = self.y/100
        self.x = int(self.x * terminalSize[1])
        self.width = int(width / 100 * terminalSize[0])
        self.height = int(height / 100 * terminalSize[1])
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