import curses

class DefaultTheme:
    def init_colors(self):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_WHITE, -1)

    def get_color(self, name: str):
        return {
            "primary": curses.color_pair(1),
            "secondary": curses.color_pair(2),
            "default": curses.color_pair(3)
        }.get(name, curses.color_pair(3))

class DarkTheme(DefaultTheme):
    def init_colors(self):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, -1)
