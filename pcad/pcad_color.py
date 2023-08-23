import sys
sys.path.append("../")

# color class for pcad

class RGBColor:
    BLACK = (0, 0, 0)
    DARK_GREY = (64, 64, 64)
    GREY = (128, 128, 128)
    LIGHT_GREY = (192, 192, 192)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PINK = (255, 192, 203)
    MAGENTA = (255, 0, 255)
    DARK_RED = (139, 0, 0)
    DARK_GREEN = (0, 100, 0)
    DARK_BLUE = (0, 0, 139)
    LIGHT_RED = (255, 99, 71)
    LIGHT_GREEN = (144, 238, 144)
    LIGHT_BLUE = (135, 206, 235)

    COLORS = [BLACK, DARK_GREY, GREY, LIGHT_GREY, WHITE, RED, GREEN, BLUE, YELLOW, PINK, MAGENTA,
              DARK_RED, DARK_GREEN, DARK_BLUE, LIGHT_RED, LIGHT_GREEN, LIGHT_BLUE]

    def __init__(self, color=None):
        if color is None:
            self.color = RGBColor.LIGHT_GREY
        else:
            self.color = color

    def set_color(self, color):
        if color in RGBColor.COLORS:
            self.color = color
        else:
            self.color = tuple(color)

    def get_color(self):
        return self.color

    def get_color_float(self):
          return tuple(c / 255.0 for c in self.color)
