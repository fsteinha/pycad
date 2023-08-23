"""Scad strategy for cube
"""
import sys
sys.path.append("../../")

from obj.primitives.obj_sphere import sphere
from const.const_strat import const_strat_base

class sphere_const_scad(const_strat_base):
    """singleton class for sphere scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_sphere:sphere):
        """proceed the scad sphere

        Args:
            a_sphere (sphere): sphere data object
        """
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_sphere.get_name()}\n"
        self.s_out = self.s_out + f"color([{a_sphere.color.get_color_float()[0]},{a_sphere.color.get_color_float()[1]},{a_sphere.color.get_color_float()[2]}])"
        self.s_out = self.s_out + f"translate([{a_sphere.pos.x},{a_sphere.pos.y},{a_sphere.pos.z}])"
        self.s_out = self.s_out + f"rotate([{a_sphere.rot.ax},{a_sphere.rot.ay},{a_sphere.rot.az}])"
        self.s_out = self.s_out + f"sphere(r={a_sphere.dr}, $fn=100);\n"
