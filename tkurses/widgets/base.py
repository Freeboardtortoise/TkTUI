from typing import Optional
import os

class Widget:
    def __init__(self, x: int, y: int, width: Optional[int] = None, height: Optional[int] = None):
        terminalSize = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        # set percentagses
        self.px=x
        self.py=y
        self.pw=width
        self.ph=height
        # set percentage
        self.x = int(x * terminalSize[0] / 100)
        self.y = int(y * terminalSize[1] / 100)
        self.width = int(width * terminalSize[0] / 100)
        self.height = int(height * terminalSize[1] / 100)
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
    
    def update(self):
        terminalSize = [os.get_terminal_size().columns, os.get_terminal_size().lines]
        # set percentagses

        # set percentage
        self.x = int(self.px * terminalSize[0] / 100)
        self.y = int(self.py * terminalSize[1] / 100)
        self.width = int(self.pw * terminalSize[0] / 100)
        self.height = int(self.ph * terminalSize[1] / 100)