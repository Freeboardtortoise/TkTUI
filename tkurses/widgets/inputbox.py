from .base import Widget
import curses
from curses.textpad import rectangle
typeable_chars = [chr(i) for i in range(32, 127)]
ENTER_KEYS = ['\n', '\r', 10, 13, curses.KEY_ENTER]
BACKSPACE_KEYS = ['\b', '\x7f', 8, 127, curses.KEY_BACKSPACE]

class InputBox(Widget):
    def __init__(self, title,x,y,width,height):
        super().__init__(x,y)
        self.text=""
        self.size = [width,height]
        self.title=title
        self.done = False
    def render(self):
        self.app.theme.get_color("default")
        rectangle(self.app.stdscr,self.y,self.x,self.y+self.size[1],self.x+self.size[0])
        self.app.stdscr.addstr(self.y,self.x+2,self.title)
        self.app.stdscr.addstr(self.y+1,self.x+1,self.text)
    def handle_input(self,key):
        if self.done == False:
            if key in typeable_chars or chr(key) in typeable_chars:
                self.text = self.text + chr(key)
            if key in BACKSPACE_KEYS:
                self.text = self.text[:-1]
            if key in ENTER_KEYS:
                self.done = True
        else:
            return self.text