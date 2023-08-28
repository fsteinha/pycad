"""Scad strategy for additive composite object
"""
import sys
sys.path.append("../../")

from obj.composites.obj_composite import aobj
from const.const_strat import const_strat_base

class aobj_const_scad(const_strat_base):
    """singleton class for cube scad strategy

    Args:
        const_strat_base (_type_): parent class
    """
    def __init__(self) -> None:
        super().__init__()

    def proceed(self, a_obj:aobj):
        """proceed the scad aobj

        Args:
            a_obj (aobj): aobj data object
        """
        s_out = "\n"
        s_out += f"//{a_obj.get_name()}\n"

        args = ("m_" + a_obj.get_name(),
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.pos.x,a_obj.pos.y,a_obj.pos.z,
                a_obj.rot.ax,a_obj.rot.ay,a_obj.rot.az)
        s_out += "module {0}()".format(*args)
        s_out += "{\n"
        l_obj = a_obj.get()
        for i_obj in l_obj:
            s_out += i_obj.const.proceed(i_obj)
        s_out += "};\n"
        s_out += "translate([{4},{5},{6}]) rotate([{7},{8},{9}]) {0}();\n".format(*args)
        return s_out

