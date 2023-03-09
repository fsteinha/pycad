import math

class Point:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)


    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)
class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        x1, y1, z1 = self.start_point.x, self.start_point.y, self.start_point.z
        x2, y2, z2 = self.end_point.x, self.end_point.y, self.end_point.z
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

    def midpoint(self):
        x1, y1, z1 = self.start_point.x, self.start_point.y, self.start_point.z
        x2, y2, z2 = self.end_point.x, self.end_point.y, self.end_point.z
        return Point((x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2)
class Dimensioning:
    AUX_LINE_LENGHT = 10
    LINE_OFFSET = 2
    TEXT_OFFSET = 2
    TEXT_SIZE = 1

    def __init__(self, start_point:Point, end_point:Point, length=None, plane="xy", name = None, text = None) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.plane = plane
        self.aux_line_start = None
        self.aux_line_end = None
        self.line:Line = None
        self.name = name
        self.textpoint = None
        self.text = text
        self.draw()

    def calculate_length(self, start_point:Point, end_point:Point):
        x1 = start_point.x
        y1 = start_point.y
        z1 = start_point.z

        x2 = end_point.x
        y2 = end_point.y
        z2 = end_point.z
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    def get_name(self) -> str:
        if self.name == None:
            self.name = str(id(self))
        return self.name

    def draw(self):
        match self.plane:
            case "xy":
                self.draw_xy()
                pass
            case "-xy":
                self.draw_nxy()
                pass
            case "yx":
                self.draw_yx()
                pass
            case "-yx":
                self.draw_nyx()
                pass
            case "xz":
                self.draw_xz()
                pass
            case "-xz":
                self.draw_nxz()
                pass
            case "zx":
                self.draw_zx()
                pass
            case "-zx":
                self.draw_nzx()
                pass
            case "yz":
                self.draw_yz()
                pass
            case "-yz":
                self.draw_nyz()
                pass
            case "zy":
                self.draw_zy()
                pass
            case "-zy":
                self.draw_nzy()
                pass
            case other:
                raise ValueError("Invalid plane type. Must be 'x', 'y', or 'z'.")

        if self.text == None:
            self.text = str(self.length)

        pass

    def level_min(self, a,b):
        if a < b:
            return a, a
        else:
            return b, b

    def level_max(self, a,b):
        if a < b:
            return b, b
        else:
            return a, a


    def draw_yx(self):
        as_ep_y = self.start_point.y + self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y + self.AUX_LINE_LENGHT

        as_ep_y, ae_ep_y = self.level_max(as_ep_y, ae_ep_y)

        as_ep = Point(self.start_point.x,
                      as_ep_y,
                      self.start_point.z)

        ae_ep = Point(self.end_point.x,
                      ae_ep_y,
                      self.start_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)
        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(0,self.LINE_OFFSET,0),
                                   ae_ep - Point(0,self.LINE_OFFSET,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,self.TEXT_OFFSET,0)
        pass

    def draw_nyx(self):
        as_ep_y = self.start_point.y - self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y - self.AUX_LINE_LENGHT

        as_ep_y, ae_ep_y = self.level_min(as_ep_y, ae_ep_y)

        as_ep = Point(self.start_point.x,
                      as_ep_y,
                      self.start_point.z)

        ae_ep = Point(self.end_point.x,
                      ae_ep_y,
                      self.start_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)
        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(0,self.LINE_OFFSET,0),
                                   ae_ep + Point(0,self.LINE_OFFSET,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() - Point(0,self.TEXT_OFFSET,0)
        pass

    def draw_xy(self):
        as_ep_x = self.start_point.x + self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x + self.AUX_LINE_LENGHT

        as_ep_x, ae_ep_x = self.level_max(as_ep_x, ae_ep_x)

        as_ep = Point(as_ep_x,
                        self.start_point.y,
                        self.start_point.z)

        ae_ep = Point(ae_ep_x,
                        self.end_point.y,
                        self.end_point.z)


        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(self.LINE_OFFSET,0,0),
                                   ae_ep - Point(self.LINE_OFFSET,0,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(self.TEXT_OFFSET,0,0)
        pass

    def draw_nxy(self):
        as_ep_x = self.start_point.x - self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x - self.AUX_LINE_LENGHT

        as_ep_x, ae_ep_x = self.level_min(as_ep_x, ae_ep_x)

        as_ep = Point(as_ep_x,
                        self.start_point.y,
                        self.start_point.z)

        ae_ep = Point(ae_ep_x,
                        self.end_point.y,
                        self.end_point.z)


        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(self.LINE_OFFSET,0,0),
                                   ae_ep + Point(self.LINE_OFFSET,0,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() - Point(self.TEXT_OFFSET,0,0)
        pass

    def draw_xz(self):
        as_ep_x = self.start_point.x + self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x + self.AUX_LINE_LENGHT

        as_ep_x, ae_ep_x = self.level_max(as_ep_x, ae_ep_x)

        as_ep = Point(as_ep_x,
                        self.start_point.y,
                        self.start_point.z)

        ae_ep = Point(ae_ep_x,
                        self.end_point.y,
                        self.end_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)
        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(self.LINE_OFFSET,0,0),
                                   ae_ep - Point(self.LINE_OFFSET,0,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(self.TEXT_OFFSET,0,0)
        pass

    def draw_nxz(self):
        as_ep_x = self.start_point.x - self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x - self.AUX_LINE_LENGHT

        as_ep_x, ae_ep_x = self.level_min(as_ep_x, ae_ep_x)

        as_ep = Point(as_ep_x,
                        self.start_point.y,
                        self.start_point.z)

        ae_ep = Point(ae_ep_x,
                        self.end_point.y,
                        self.end_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)
        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(self.LINE_OFFSET,0,0),
                                   ae_ep + Point(self.LINE_OFFSET,0,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() - Point(self.TEXT_OFFSET,0,0)
        pass

    def draw_zx(self):
        as_ep_z = self.start_point.z + self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z + self.AUX_LINE_LENGHT

        as_ep_z, ae_ep_z = self.level_max(as_ep_z, ae_ep_z)

        as_ep = Point(self.start_point.x,
                        self.start_point.y,
                        as_ep_z)

        ae_ep = Point(self.end_point.x,
                        self.end_point.y,
                        ae_ep_z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(0,0,self.LINE_OFFSET),
                                   ae_ep - Point(0,0,self.LINE_OFFSET))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,0,self.TEXT_OFFSET)
        pass

    def draw_nzx(self):
        as_ep_z = self.start_point.z - self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z - self.AUX_LINE_LENGHT

        as_ep_z, ae_ep_z = self.level_min(as_ep_z, ae_ep_z)

        as_ep = Point(self.start_point.x,
                        self.start_point.y,
                        as_ep_z)

        ae_ep = Point(self.end_point.x,
                        self.end_point.y,
                        ae_ep_z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(0,0,self.LINE_OFFSET),
                                   ae_ep + Point(0,0,self.LINE_OFFSET))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,0,self.TEXT_OFFSET)
        pass

    def draw_zy(self):
        as_ep_z = self.start_point.z + self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z + self.AUX_LINE_LENGHT

        as_ep_z, ae_ep_z = self.level_max(as_ep_z, ae_ep_z)

        as_ep = Point(self.start_point.x,
                        self.start_point.y,
                        as_ep_z)

        ae_ep = Point(self.end_point.x,
                        self.end_point.y,
                        ae_ep_z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(0,0,self.LINE_OFFSET),
                                   ae_ep - Point(0,0,self.LINE_OFFSET))


        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,0,self.TEXT_OFFSET)
        pass

    def draw_nzy(self):
        as_ep_z = self.start_point.z - self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z - self.AUX_LINE_LENGHT

        as_ep_z, ae_ep_z = self.level_min(as_ep_z, ae_ep_z)

        as_ep = Point(self.start_point.x,
                        self.start_point.y,
                        as_ep_z)

        ae_ep = Point(self.end_point.x,
                        self.end_point.y,
                        ae_ep_z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(0,0,self.LINE_OFFSET),
                                   ae_ep + Point(0,0,self.LINE_OFFSET))


        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,0,self.TEXT_OFFSET)
        pass

    def draw_yz(self):
        as_ep_y = self.start_point.y + self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y + self.AUX_LINE_LENGHT

        as_ep_y, ae_ep_y = self.level_max(as_ep_y, ae_ep_y)

        as_ep = Point(self.start_point.x,
                        as_ep_y,
                        self.start_point.z)

        ae_ep = Point(self.end_point.x,
                        ae_ep_y,
                        self.end_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep - Point(0,self.LINE_OFFSET,0),
                                   ae_ep - Point(0,self.LINE_OFFSET,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() + Point(0,self.TEXT_OFFSET,0)
        pass

    def draw_nyz(self):
        as_ep_y = self.start_point.y - self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y - self.AUX_LINE_LENGHT

        as_ep_y, ae_ep_y = self.level_min(as_ep_y, ae_ep_y)

        as_ep = Point(self.start_point.x,
                        as_ep_y,
                        self.start_point.z)

        ae_ep = Point(self.end_point.x,
                        ae_ep_y,
                        self.end_point.z)

        self.aux_line_start = Line(self.start_point, as_ep)

        self.aux_line_end   = Line(self.end_point, ae_ep)

        self.line           = Line(as_ep + Point(0,self.LINE_OFFSET,0),
                                   ae_ep + Point(0,self.LINE_OFFSET,0))

        self.length = self.calculate_length(as_ep, ae_ep)
        self.textpoint = self.line.midpoint() -  Point(0,self.TEXT_OFFSET,0)
        pass
