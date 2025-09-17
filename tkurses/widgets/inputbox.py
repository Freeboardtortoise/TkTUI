from .base import Widget
import curses
from curses.textpad import rectangle
typeable_chars = [chr(i) for i in range(32, 127)]
ENTER_KEYS = ['\n', '\r', 10, 13, curses.KEY_ENTER]
BACKSPACE_KEYS = ['\b', '\x7f', 8, 127, curses.KEY_BACKSPACE]

class InputBox(Widget):
    def __init__(self, title,pos,size,on_press):
        super().__init__(pos[0],pos[1])
        self.text=""
        self.size = size
        self.title=title
        self.done = False
        self.on_press = on_press
    def render(self):
        theme = self.app.theme.get_input_theme()
        if self.focused:
            color = self.app.theme.getColors()["inputs"]["focused"]
        else:
            color = self.app.theme.getColors()["inputs"]["not-focused"]
        style = theme["style"]
        if style == "box":
            rectangle(self.app.stdscr,self.y,self.x,self.y+self.size[1],self.x+self.size[0])
            self.app.stdscr.addstr(self.y,self.x+2,self.title,curses.color_pair(color))
            self.app.stdscr.addstr(self.y+1,self.x+1,self.text,curses.color_pair(color))
        if style == "pinput":
            self.app.stdscr.addstr(self.y,self.x+2,self.title+": ",curses.color_pair(color))
            self.app.stdscr.addstr(self.y,self.x+len(self.title),curses.color_pair(color))
    def handle_input(self,key):
        if self.done == False:
            if key in typeable_chars or chr(key) in typeable_chars:
                self.text = self.text + chr(key)
            if key in BACKSPACE_KEYS:
                self.text = self.text[:-1]
            if key in ENTER_KEYS:
                self.on_press(self.text)
        else:
            return self.text