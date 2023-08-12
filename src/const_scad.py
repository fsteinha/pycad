from const import *
from pcad_obj import *
from pcad_primitives import *
import subprocess

class scad_const(const):
    def __init__(self, name, *l_obj) -> None:
        super().__init__(name, *l_obj)
        self.s_out = ""
        self.s_filename += ".scad"
        self.s_ecall = "openscad"

    def show(self):
        self.iterate_obj(self.l_obj)
        f_file = open(self.s_filename, "w")
        f_file.write(self.s_out)
        f_file.close()
        print(f"{self.s_filename} created")
        s_call = f"{self.s_ecall} {self.s_filename}"
        print (s_call)
        p = subprocess.Popen([self.s_ecall, self.s_filename], stdout = subprocess.PIPE)
        print ("scad started")
        #p.wait()

    def cube(self, a_cube:cube):
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_cube.get_name()}\n"
        self.s_out = self.s_out + f"color([{a_cube.color.get_color_float()[0]},{a_cube.color.get_color_float()[1]},{a_cube.color.get_color_float()[2]}])translate([{a_cube.pos.x},{a_cube.pos.y},{a_cube.pos.z}]) rotate([{a_cube.rot.ax},{a_cube.rot.ay},{a_cube.rot.az}]) cube([{a_cube.dx},{a_cube.dy},{a_cube.dz}]);\n"

    def cylinder(self, a_cylinder:cylinder):
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_cylinder.get_name()}\n"
        self.s_out = self.s_out + f"color([{a_cylinder.color.get_color_float()[0]},{a_cylinder.color.get_color_float()[1]},{a_cylinder.color.get_color_float()[2]}])translate([{a_cylinder.pos.x},{a_cylinder.pos.y},{a_cylinder.pos.z}]) rotate([{a_cylinder.rot.ax},{a_cylinder.rot.ay},{a_cylinder.rot.az}]) cylinder(h={a_cylinder.dh},r1={a_cylinder.drb},r2={a_cylinder.drt}, $fn=100);\n"

    def aobj(self, a_obj:cobj):
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_obj.get_name()}\n"

        args = ("m_" + a_obj.get_name(),
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.rot.ax,a_obj.rot.ay,a_obj.rot.az)
        self.s_out = self.s_out + "module {0}()".format(*args)
        self.s_out = self.s_out + "{\n"
        self.iterate_obj(a_obj.get())
        self.s_out = self.s_out + "};\n"
        self.s_out = self.s_out + "translate([{4},{5},{6}]) rotate([{7},{8},{9}]) {0}();\n".format(*args)

    def sobj(self, a_obj:sobj):
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_obj.get_name()}\n"

        s_module = "m_" + a_obj.get_name()
        self.s_out = self.s_out + f"module {s_module}()"
        self.s_out = self.s_out + "{\n"
        self.s_out = self.s_out + "  difference(){\n"
        self.iterate_obj(a_obj.get())
        self.s_out = self.s_out + "  };\n"
        self.s_out = self.s_out + "};\n"
        self.s_out = self.s_out + f"color([{a_obj.color.get_color_float()[0]},{a_obj.color.get_color_float()[1]},{a_obj.color.get_color_float()[2]}]) translate([{a_obj.pos.x},{a_obj.pos.y},{a_obj.pos.z}]) rotate([{a_obj.rot.ax},{a_obj.rot.ay},{a_obj.rot.az}]) {s_module}();\n"

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
                a_dim.prop.text_size)

        self.s_out = self.s_out + "module {0}()".format(*args)
        self.s_out = self.s_out + "{\n"
        self.s_out = self.s_out + f"   module line(start, end, thickness = {a_dim.prop.line_thickness})\n"
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
