import sys
import copy

sys.path.append("../..")
from pcad import pcad_obj, pcad_pos
from const import const_obj

class cylinder_const(const_obj.const_obj_base):
    pass

class cylinder(pcad_obj.obj):
    def __init__(self,  drb:float=10.0, drt:float = 10.0, dh:float=10.0, name = None, pos:pcad_pos.pos=pcad_pos.pos(), rot:pcad_pos.rot=pcad_pos.rot()) -> None:
        super().__init__(name, pos, rot)
        self.drb = drb
        self.drt = drt
        self.dh  = dh
        self.const = cylinder_const()

    def copy(self):
        ret = copy.deepcopy(self)
        ret.const = cylinder_const()
        return ret


