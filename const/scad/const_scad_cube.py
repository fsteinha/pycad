"""Scad strategy for cube
"""
import sys
sys.path.append("../../")

from obj.primitives.obj_cube import cube
from const.const_strat import const_strat_base

class cube_const_scad(const_strat_base):
    """singleton class for cube scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_cube:cube):
        """proceed the scad cube

        Args:
            a_cube (cube): cube data object
        """
        self.s_out = self.s_out + "\n"
        self.s_out = self.s_out + f"//{a_cube.get_name()}\n"
        self.s_out = self.s_out + f"color([{a_cube.color.get_color_float()[0]},{a_cube.color.get_color_float()[1]},{a_cube.color.get_color_float()[2]}])"
        self.s_out = self.s_out + f"translate([{a_cube.pos.x},{a_cube.pos.y},{a_cube.pos.z}])"
        self.s_out = self.s_out + f"rotate([{a_cube.rot.ax},{a_cube.rot.ay},{a_cube.rot.az}])"
        self.s_out = self.s_out + f"cube([{a_cube.dx},{a_cube.dy},{a_cube.dz}]);\n"
