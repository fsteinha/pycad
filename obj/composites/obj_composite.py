import sys
sys.path.append("../..")

from pcad.pcad_obj import obj
from pcad.pcad_pos import pos, rot
from pcad.pcad_purch import purch
from obj.dimension.obj_dim import Dimensioning

from const import const_obj

class aobj_const(const_obj.const_obj_base):
    """base singleton class for all const classes for aobj
    """
    pass

class sobj_const(const_obj.const_obj_base):
    """base singleton class for all const classes for sobj
    """
    pass

class cobj(obj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), info:str="", purch=purch, *args) -> None:
        super().__init__(name=name, pos=pos, rot=rot, info=info, purch=purch)
        self.l_obj = []
        for arg in args:
            self.add(arg)
        pass

    def add(self, a_obj) -> bool:
        if isinstance(a_obj, obj) or \
            isinstance(a_obj, Dimensioning):
            self.l_obj.append(a_obj)
        else:
            raise Exception(f"Not allowed type {type(a_obj)}")
        return True

    def get(self) -> list:
        return self.l_obj


class aobj(cobj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), info:str="", purch:purch=None, *args) -> None:
        super().__init__(name=name, pos=pos, rot=rot, info=info, purch=purch, *args)
        self.const = aobj_const()
        pass

class sobj(cobj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), info:str="", purch:purch=None, *args) -> None:
        super().__init__(name=name, pos=pos, rot=rot, info=info, purch=purch, *args)
        self.const = sobj_const()
        pass