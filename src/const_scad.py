from const import *
from pcad_obj import *
from pcad_primitives import *
import subprocess

class scad(const):
    def __init__(self, name, *l_obj) -> None:
        super().__init__(name, *l_obj)
        self.s_out = ""
        self.s_filename = name + ".scad"
        self.s_ecall = "openscad"

    def show(self):
        self.iterate_obj(self.l_obj)
        f_file = open(self.s_filename, "w")
        f_file.write(self.s_out)
        f_file.close()
        s_call = f"{self.s_ecall} {self.s_filename}"
        print (s_call)
        p = subprocess.Popen([self.s_ecall, self.s_filename], stdout = subprocess.PIPE)
        #p.wait()

    def iterate_obj(self, l_obj):
        for i_obj in l_obj:
            if isinstance(i_obj, cube):
                self.cube(i_obj)
            elif isinstance(i_obj, cobj):
                self.cobj(i_obj)
            elif isinstance(i_obj, dim.Dimensioning):
                self.dim(i_obj)
            else:
                raise Exception (f"Unknown {type(i_obj)}")


    def cube(self, a_cube:cube):
        args = ("m_" + a_cube.get_name(),
                a_cube.dx,a_cube.dy,a_cube.dz,
                a_cube.pos.x,a_cube.pos.y,a_cube.pos.z,
                a_cube.rot.ax,a_cube.rot.ay,a_cube.rot.az)
        self.s_out = self.s_out + "module {0}()".format(*args)
        self.s_out = self.s_out + "{\n"
        self.s_out = self.s_out + "   cube([{1},{2},{3}]);\n".format(*args)
        self.s_out = self.s_out + "};\n"
        self.s_out = self.s_out + "translate([{4},{5},{6}]) rotate([{7},{8},{9}]) {0}();\n".format(*args)

    def cobj(self, a_obj:cobj):
        args = ("m_" + a_obj.get_name(),
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.rot.ax,a_obj.rot.ay,a_obj.rot.az)
        self.s_out = self.s_out + "module {0}()".format(*args)
        self.s_out = self.s_out + "{\n"
        self.iterate_obj(a_obj.get())
        self.s_out = self.s_out + "};\n"
        self.s_out = self.s_out + "translate([{4},{5},{6}]) rotate([{7},{8},{9}]) {0}();\n".format(*args)

    def dim(self, a_dim:dim.Dimensioning):
        args = ("m_dim_" + a_dim.get_name(),
                a_dim.aux_line_start.start_point.x,
                a_dim.aux_line_start.start_point.y,
                a_dim.aux_line_start.start_point.z,

                a_dim.aux_line_start.end_point.x,
                a_dim.aux_line_start.end_point.y,
                a_dim.aux_line_start.end_point.z,

                a_dim.aux_line_end.start_point.x,
                a_dim.aux_line_end.start_point.y,
                a_dim.aux_line_end.start_point.z,

                a_dim.aux_line_end.end_point.x,
                a_dim.aux_line_end.end_point.y,
                a_dim.aux_line_end.end_point.z,

                a_dim.line.start_point.x,
                a_dim.line.start_point.y,
                a_dim.line.start_point.z,

                a_dim.line.end_point.x,
                a_dim.line.end_point.y,
                a_dim.line.end_point.z,

                a_dim.textpoint.x,
                a_dim.textpoint.y,
                a_dim.textpoint.z,

                a_dim.text,
                a_dim.TEXT_SIZE)

        self.s_out = self.s_out + "module {0}()".format(*args)
        self.s_out = self.s_out + "{\n"
        self.s_out = self.s_out + "   module line(start, end, thickness = 0.1)\n"
        self.s_out = self.s_out + "   {\n"
        self.s_out = self.s_out + "         hull()\n"
        self.s_out = self.s_out + "         {\n"
        self.s_out = self.s_out + "            translate(start) sphere(thickness);\n"
        self.s_out = self.s_out + "            translate(end) sphere(thickness);\n"
        self.s_out = self.s_out + "         }\n"
        self.s_out = self.s_out + "   }\n"
        self.s_out = self.s_out + "   line([{1},{2},{3}],[{4},{5},{6}]);\n".format(*args)
        self.s_out = self.s_out + "   line([{7},{8},{9}],[{10},{11},{12}]);\n".format(*args)
        self.s_out = self.s_out + "   line([{13},{14},{15}],[{16},{17},{18}]);\n".format(*args)
        match a_dim.plane:
            case "yx":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-yx":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,180,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "xy":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-xy":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,0,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "zx":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-zx":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "xz":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-xz":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "yz":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-yz":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "zy":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-zy":
                self.s_out = self.s_out + "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)

            case other:
                raise Exception (f"Unknown plan {a_dim.plane}")

        self.s_out = self.s_out + "};\n"
        self.s_out = self.s_out + "color(\"black\") {0}();\n".format(*args)

        pass
