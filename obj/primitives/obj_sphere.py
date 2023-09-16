import sys
sys.path.append("../..")
from pcad import pcad_obj, pcad_pos
from const import const_obj

class sphere_const(const_obj.const_obj_base):
    pass

class sphere(pcad_obj.obj):
    def __init__(self, dr:float = 10.0, name = None, pos:pcad_pos.pos=pcad_pos.pos(), rot:pcad_pos.rot=pcad_pos.rot()) -> None:
        super().__init__(name, pos, rot)
        self.dr = dr
        self.const = sphere_const()


