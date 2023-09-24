import sys
import copy

sys.path.append("../..")
from pcad import pcad_obj, pcad_pos
from const import const_obj

class cube_const(const_obj.const_obj_base):
    pass

class cube(pcad_obj.obj):
    def __init__(self, dx:float=10.0, dy:float=10.0, dz:float=10.0, name = None, pos:pcad_pos.pos=pcad_pos.pos(), rot:pcad_pos.rot=pcad_pos.rot()) -> None:
        super().__init__(name, pos, rot)
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.const = cube_const()

    def copy(self):
        ret = copy.deepcopy(self)
        ret.const = cube_const()
        return ret

