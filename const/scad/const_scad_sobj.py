"""Scad strategy for additive composite object
"""
import sys
sys.path.append("../../")

from obj.composites.obj_composite import sobj
from const.const_strat import const_strat_base

class sobj_const_scad(const_strat_base):
    """singleton class for cube scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_obj:sobj):
        """proceed the scad sobj

        Args:
            s_obj (sobj): sobj data object
        """
        s_out =  "\n"
        s_out +=  f"//{a_obj.get_name()}\n"

        s_module = "m_" + a_obj.get_name()
        s_out +=  f"module {s_module}()"
        s_out +=  "{\n"
        s_out +=  "  difference(){\n"
        l_obj = a_obj.get()
        for i_obj in l_obj:
            s_out += i_obj.const.proceed(i_obj)
        s_out +=  "  };\n"
        s_out +=  "};\n"
        s_out +=  f"color([{a_obj.color.get_color_float()[0]},{a_obj.color.get_color_float()[1]},{a_obj.color.get_color_float()[2]}]) translate([{a_obj.pos.x},{a_obj.pos.y},{a_obj.pos.z}]) rotate([{a_obj.rot.ax},{a_obj.rot.ay},{a_obj.rot.az}]) {s_module}();\n"
        return s_out


