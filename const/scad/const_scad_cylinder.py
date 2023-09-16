"""Scad strategy for cube
"""
import sys
sys.path.append("../../")

from obj.primitives.obj_cylinder import cylinder
from const.const_strat import const_strat_base

class cylinder_const_scad(const_strat_base):
    """singleton class for cylinder scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_cylinder:cylinder):
        """proceed the scad cylinder

        Args:
            a_cylinder (cylinder): cylinder data object
        """
        s_out = "\n"
        s_out +=  f"//{a_cylinder.get_name()}\n"
        s_out +=  f"color([{a_cylinder.color.get_color_float()[0]},{a_cylinder.color.get_color_float()[1]},{a_cylinder.color.get_color_float()[2]}])"
        s_out +=  f"translate([{a_cylinder.pos.x},{a_cylinder.pos.y},{a_cylinder.pos.z}])"
        s_out +=  f"rotate([{a_cylinder.rot.ax},{a_cylinder.rot.ay},{a_cylinder.rot.az}])"
        s_out +=  f"cylinder(h={a_cylinder.dh},r1={a_cylinder.drb},r2={a_cylinder.drt}, $fn=100);\n"
        return s_out
