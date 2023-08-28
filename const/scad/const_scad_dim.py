"""Scad strategy for additive composite object
"""
import sys
sys.path.append("../../")

from obj.dimension.obj_dim import Dimensioning
from const.const_strat import const_strat_base

class dim_const_scad(const_strat_base):
    """singleton class for dim scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_dim:Dimensioning):
        """proceed the scad Dimensioning

        Args:
            a_dim (Dimensioning): Dimensioning data object
        """
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

        s_out = "module {0}()".format(*args)
        s_out +=  "{\n"
        s_out +=  f"   module line(start, end, thickness = {a_dim.prop.line_thickness})\n"
        s_out +=  "   {\n"
        s_out +=  "         hull()\n"
        s_out +=  "         {\n"
        s_out +=  "            translate(start) sphere(thickness);\n"
        s_out +=  "            translate(end) sphere(thickness);\n"
        s_out +=  "         }\n"
        s_out +=  "   }\n"
        s_out +=  "   line([{1},{2},{3}],[{4},{5},{6}]);\n".format(*args)
        s_out +=  "   line([{7},{8},{9}],[{10},{11},{12}]);\n".format(*args)
        s_out +=  "   line([{13},{14},{15}],[{16},{17},{18}]);\n".format(*args)
        match a_dim.plane:
            case "yx":
                s_out +=  "   translate([{19},{20},{21}]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-yx":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([0,180,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "xy":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([0,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-xy":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([0,0,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "zx":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-zx":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,0,0]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "xz":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-xz":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([0,270,90]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "yz":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-yz":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,270,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "zy":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)
            case "-zy":
                s_out +=  "   translate([{19},{20},{21}]) rotate ([90,0,270]) linear_extrude (height = 0.1) {{text(\"{22}\", size={23}, halign=\"center\");}}\n".format(*args)

            case other:
                raise Exception (f"Unknown plan {a_dim.plane}")

        s_out +=  "};\n"
        s_out +=  "color(\"black\") {0}();\n".format(*args)
        return s_out
        pass



