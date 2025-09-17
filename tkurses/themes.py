import curses
import curses

COLOR_MAP = {
    "black": curses.COLOR_BLACK,
    "red": curses.COLOR_RED,
    "green": curses.COLOR_GREEN,
    "yellow": curses.COLOR_YELLOW,
    "blue": curses.COLOR_BLUE,
    "magenta": curses.COLOR_MAGENTA,
    "cyan": curses.COLOR_CYAN,
    "white": curses.COLOR_WHITE
}

def convert_colors(config):
    if isinstance(config, dict):
        new_dict = {}
        for k, v in config.items():
            if isinstance(v, str):
                lower_v = v.lower()
                # Replace if the string matches a color name
                if lower_v in COLOR_MAP:
                    new_dict[k] = COLOR_MAP[lower_v]
                else:
                    new_dict[k] = v
            else:
                new_dict[k] = convert_colors(v)
        return new_dict
    elif isinstance(config, list):
        return [convert_colors(item) for item in config]
    else:
        return config

class ThemeManager:
    def __init__(self, themeFile):
        import json
        curses.start_color()
        with open(themeFile,"r") as file:
            data = json.load(file)
        self.data = data
        self.data = convert_colors(self.data)
        curses.init_pair(1, self.data["colors"]["forground"], self.data["colors"]["background"])
    def get_input_theme(self):
        return self.data["input"]
    def get_label_theme(self):
        return self.data["text"]
    def get_button_theme(self):
        return self.data["buttons"]