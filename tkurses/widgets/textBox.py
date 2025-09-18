from .base import Widget
import curses
import curses.textpad as textpad
typeable_chars = [chr(i) for i in range(32, 127)]
ENTER_KEYS = ['\n', '\r', 10, 13, curses.KEY_ENTER]
BACKSPACE_KEYS = ['\b', '\x7f', 8, 127, curses.KEY_BACKSPACE]

class TextBox(Widget):
    def __init__(self,pos,size,exitOnEnter=True):
        super().__init__(pos[0],pos[1])
        self.size=size
        self.exitOnEnter=False
        self.text = ""
    def render(self):
        textpad.rectangle(self.app.stdscr,self.y,self.x,self.size[1]+self.x,self.x+self.seze[0])
        row=1
        for line in self.text.split("\n"):
            if len(line) >= self.size[0]:
                line=line[:self.size[0]]
            self.app.stdscr.addstr(self.y+row,self.x+1,line)
    def handle_input(self,key):
        if k
