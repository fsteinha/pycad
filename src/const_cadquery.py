from const import *
from pcad_obj import *
from pcad_primitives import *
import cadquery as cq
from cq_server.ui import ui, show_object


class cq_const(const):
    def __init__(self, name, *l_obj) -> None:
        super().__init__(name, *l_obj)
        self.s_filename += ".py"
        self.s_out =  "import cadquery as cq\n"
        self.s_out += "from cq_server.ui import ui, show_object\n"
        self.s_out += "\n"
        self.s_out += "result = cq.Workplane('XY')\n"


    def show(self):
        self.iterate_obj(self.l_obj)
        self.s_out += "show_object(result)\n"
        f_file = open(self.s_filename, "w")
        f_file.write(self.s_out)
        f_file.close()
        print(f"{self.s_filename} created")


    def cube(self, a_cube:cube):
        args = (a_cube.get_name(),
                a_cube.dx,a_cube.dy,a_cube.dz,
                a_cube.pos.x,a_cube.pos.y,a_cube.pos.z,
                a_cube.rot.ax,a_cube.rot.ay,a_cube.rot.az)

        self.s_out += "# {0}\n".format(*args)
        result = cq.Workplane('XY').box(328,6,75, centered=(False,False,False)).rotate((0,0,0),(0,-1,0),90).translate((0,0,0))

        self.s_out += "result = result.add(cq.Workplane('XY').\n"
        self.s_out += "           box({1},{2},{3}, centered=(False,False,False)).\n".format(*args)
        if (a_cube.rot.ax != 0):
            self.s_out += "       rotate((0,0,0),(1,0,0),{7}).".format(*args)
        elif (a_cube.rot.ay != 0):
            self.s_out += "       rotate((0,0,0),(0,1,0),{8}).".format(*args)
        elif (a_cube.rot.az != 0):
            self.s_out += "       rotate((0,0,0),(0,0,1),{9}).".format(*args)
        self.s_out += "           translate(({4},{5},{6})))\n".format(*args)

    def cobj(self, a_obj:cobj):
        self.iterate_obj(a_obj.get())

    def dim(self, a_dim:dim.Dimensioning):
        args = (a_dim.get_name(),
                a_dim.aux_line_start.start_point.x, # 1
                a_dim.aux_line_start.start_point.y, # 2
                a_dim.aux_line_start.start_point.z, # 3

                a_dim.aux_line_start.end_point.x,   # 4
                a_dim.aux_line_start.end_point.y,   # 5
                a_dim.aux_line_start.end_point.z,   # 6

                a_dim.aux_line_end.start_point.x,   # 7
                a_dim.aux_line_end.start_point.y,   # 8
                a_dim.aux_line_end.start_point.z,   # 9

                a_dim.aux_line_end.end_point.x,     # 10
                a_dim.aux_line_end.end_point.y,     # 11
                a_dim.aux_line_end.end_point.z,     # 12

                a_dim.line.start_point.x,           # 13
                a_dim.line.start_point.y,           # 14
                a_dim.line.start_point.z,           # 15

                a_dim.line.end_point.x,             # 16
                a_dim.line.end_point.y,             # 17
                a_dim.line.end_point.z,             # 18

                a_dim.textpoint.x,                  # 19
                a_dim.textpoint.y,                  # 20
                a_dim.textpoint.z,                  # 21

                a_dim.text,                         # 22
                a_dim.TEXT_SIZE)                    # 23

        self.s_out += f"# {a_dim.get_name()}\n"

        match a_dim.plane:
            case "yx":
                # startline
                self.s_out += f"result = result.add(cq.Workplane('XY').vLineTo({a_dim.aux_line_start.end_point.y-a_dim.aux_line_start.start_point.y}).translate(({a_dim.aux_line_start.start_point.x, a_dim.aux_line_start.start_point.y, a_dim.aux_line_start.start_point.z})))\n"
                # endline
                self.s_out += f"result = result.add(cq.Workplane('XY').vLineTo({a_dim.aux_line_end.end_point.y-a_dim.aux_line_end.start_point.y}).translate(({a_dim.aux_line_end.start_point.x, a_dim.aux_line_end.start_point.y, a_dim.aux_line_end.start_point.z})))\n"
        #     case "-yx":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,180,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "xy":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "-xy":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,0,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "zx":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "-zx":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "xz":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "-xz":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "yz":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "-yz":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "zy":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
        #     case "-zy":
        #         self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)

        #     case other:
        #         raise Exception (f"Unknown plan {a_dim.plane}")

        # self.s_out = self.s_out + "};\n"
        # self.s_out = self.s_out + "color(\"black\") {0}();\n".format(*args)

        pass
