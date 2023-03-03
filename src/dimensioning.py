class Point:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        x1, y1, z1 = self.start_point.x, self.start_point.y, self.start_point.z
        x2, y2, z2 = self.end_point.x, self.end_point.y, self.end_point.z
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


class Dimensioning:
    AUX_LINE_LENGHT = 10
    LINE_OFFSET = 2

    def __init__(self, start_point:Point, end_point:Point, length=None, plane="xy", name = None) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.plane = plane
        self.aux_line_start = None
        self.aux_line_end = None
        self.line = None
        self.name = name
        self.draw()

    def calculate_length(self):
        x1 = self.start_point.x
        y1 = self.start_point.y
        z1 = self.start_point.z

        x2 = self.end_point.x
        y2 = self.end_point.y
        z2 = self.end_point.z
        return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

    def get_name(self) -> str:
        if self.name == None:
            self.name = str(id(self))
        return self.name

    def draw(self):
        if self.length is None:
            self.calculate_length()

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
        pass

    def draw_yx(self):
        as_ep_y = self.start_point.y + self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                   Point(self.start_point.x,
                                         as_ep_y,
                                         self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         ae_ep_y,
                                         self.end_point.z))

        self.line           = Line(Point(self.start_point.x,
                                         as_ep_y-self.LINE_OFFSET,
                                         self.start_point.z),
                                    Point(self.end_point.x,
                                           ae_ep_y-self.LINE_OFFSET,
                                           self.end_point.z))
    def draw_nyx(self):
        aux_start_ep_y = self.start_point.y - self.AUX_LINE_LENGHT
        aux_end_ep_y = self.end_point.y - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(self.start_point.x,
                                          aux_start_ep_y,
                                          self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                    Point(self.end_point.x,
                                          aux_end_ep_y,
                                          self.end_point.z))

        self.line           = Line(Point(self.start_point.x,
                                         aux_start_ep_y+self.LINE_OFFSET,
                                         self.start_point.z),
                                    Point(self.end_point.x,
                                          aux_end_ep_y+self.LINE_OFFSET,
                                          self.end_point.z))
    def draw_xy(self):
        aux_start_ep_x = self.start_point.x + self.AUX_LINE_LENGHT
        aux_end_ep_x = self.end_point.x + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(aux_start_ep_x,
                                          self.start_point.y,
                                          self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(aux_end_ep_x,
                                         self.end_point.y,
                                         self.end_point.z))

        self.line           = Line(Point(aux_start_ep_x-self.LINE_OFFSET,
                                         self.start_point.y,
                                         self.start_point.z),
                                    Point(aux_end_ep_x-self.LINE_OFFSET,
                                          self.end_point.y,
                                          self.end_point.z))
    def draw_nxy(self):
        aux_start_ep_x = self.start_point.x - self.AUX_LINE_LENGHT
        aux_end_ep_x = self.end_point.x - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                   Point(aux_start_ep_x,
                                         self.start_point.y,
                                         self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(aux_end_ep_x,
                                         self.end_point.y,
                                         self.end_point.z))

        self.line           = Line(Point(aux_start_ep_x+self.LINE_OFFSET,
                                         self.start_point.y,
                                         self.start_point.z),
                                    Point(aux_end_ep_x+self.LINE_OFFSET,
                                          self.end_point.y,
                                          self.end_point.z))
    def draw_xz(self):
        as_ep_x = self.start_point.x + self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(as_ep_x,
                                          self.start_point.y,
                                          self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(ae_ep_x,
                                         self.end_point.y,
                                         self.end_point.z))

        self.line           = Line(Point(as_ep_x-self.LINE_OFFSET,
                                         self.start_point.y,
                                         self.start_point.z),
                                    Point(ae_ep_x-self.LINE_OFFSET,
                                          self.end_point.y,
                                          self.end_point.z))
        pass

    def draw_nxz(self):
        as_ep_x = self.start_point.x - self.AUX_LINE_LENGHT
        ae_ep_x = self.end_point.x - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(as_ep_x,
                                          self.start_point.y,
                                          self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(ae_ep_x,
                                         self.end_point.y,
                                         self.end_point.z))

        self.line           = Line(Point(as_ep_x+self.LINE_OFFSET,
                                         self.start_point.y,
                                         self.start_point.z),
                                    Point(ae_ep_x+self.LINE_OFFSET,
                                          self.end_point.y,
                                          self.end_point.z))
    def draw_zx(self):
        as_ep_z = self.start_point.z + self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                   Point(self.start_point.x,
                                         self.start_point.y,
                                         as_ep_z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         self.end_point.y,
                                         ae_ep_z))

        self.line           = Line(Point(self.start_point.x,
                                         self.start_point.y,
                                         as_ep_z-self.LINE_OFFSET),
                                    Point(self.end_point.x,
                                           self.end_point.y,
                                           ae_ep_z-self.LINE_OFFSET))
        pass
    def draw_nzx(self):
        as_ep_z = self.start_point.y - self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.y - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(self.start_point.x,
                                          self.start_point.y,
                                          as_ep_z))
        self.aux_line_end   = Line(self.end_point,
                                    Point(self.end_point.x,
                                          self.end_point.y,
                                          ae_ep_z))

        self.line           = Line(Point(self.start_point.x,
                                         self.start_point.y,
                                         as_ep_z+self.LINE_OFFSET),
                                    Point(self.end_point.x,
                                          self.end_point.y,
                                          ae_ep_z+self.LINE_OFFSET))
        pass
    def draw_zy(self):
        as_ep_z = self.start_point.z + self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(self.start_point.x,
                                          self.start_point.y,
                                          as_ep_z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         self.end_point.y,
                                         ae_ep_z))

        self.line           = Line(Point(self.start_point.x,
                                         self.start_point.y,
                                         as_ep_z-self.LINE_OFFSET),
                                    Point(self.end_point.x,
                                          self.end_point.y,
                                          ae_ep_z-self.LINE_OFFSET))
    def draw_nzy(self):
        as_ep_z = self.start_point.z - self.AUX_LINE_LENGHT
        ae_ep_z = self.end_point.z - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                    Point(self.start_point.x,
                                          self.start_point.y,
                                          as_ep_z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         self.end_point.y,
                                         ae_ep_z))

        self.line           = Line(Point(self.start_point.x,
                                         self.start_point.y,
                                         as_ep_z+self.LINE_OFFSET),
                                    Point(self.end_point.x,
                                          self.end_point.y,
                                          ae_ep_z+self.LINE_OFFSET))
    def draw_yz(self):
        as_ep_y = self.start_point.y + self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y + self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                   Point(self.start_point.x,
                                         as_ep_y,
                                         self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         ae_ep_y,
                                         self.end_point.z))

        self.line           = Line(Point(self.start_point.x,
                                         as_ep_y-self.LINE_OFFSET,
                                         self.start_point.z),
                                    Point(self.end_point.x,
                                           ae_ep_y-self.LINE_OFFSET,
                                           self.end_point.z))
    def draw_nyz(self):
        as_ep_y = self.start_point.y - self.AUX_LINE_LENGHT
        ae_ep_y = self.end_point.y - self.AUX_LINE_LENGHT

        self.aux_line_start = Line(self.start_point,
                                   Point(self.start_point.x,
                                         as_ep_y,
                                         self.start_point.z))
        self.aux_line_end   = Line(self.end_point,
                                   Point(self.end_point.x,
                                         ae_ep_y,
                                         self.end_point.z))

        self.line           = Line(Point(self.start_point.x,
                                         as_ep_y+self.LINE_OFFSET,
                                         self.start_point.z),
                                    Point(self.end_point.x,
                                           ae_ep_y+self.LINE_OFFSET,
                                           self.end_point.z))
