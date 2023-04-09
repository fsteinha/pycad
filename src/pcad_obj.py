from pcad_pos import pos, rot
from pcad_color import RGBColor
import dimensioning as dim
import gc


class obj:
    def __init__(self, name:str = None, pos:pos=pos(),rot:rot=rot(), color:RGBColor = RGBColor()) -> None:
        self.pos = pos
        self.rot = rot
        self.set_name(name)
        self.set_color(color)
        pass

    def mov(self, mx=0, my=0, mz=0) -> None:
        self.pos.mov(mx, my, mz)
        pass

    def rot(self, ax=0, ay=0, az=0) -> None:
        self.rot.rot(ax, ay, az)
        pass

    def set_name(self, name) -> None:
        if name == None:
            self.name = None
            for obj in gc.get_referrers(self):
                if isinstance(obj, dict):
                    for obj_name, value in obj.items():
                        if value is self:
                            self.name = obj_name
        else:
            self.name = name
        pass

    def get_name(self) -> str:
        return self.name

    def set_color(self,color):
        if (color in RGBColor.COLORS):
            self.color = RGBColor(color)
        elif (isinstance(color, RGBColor)):
            self.color = color
        else:
            raise Exception(f"Not RGBColor object or an color setting {type(color)}")



class pobj(obj):
    def __init__(self, pos: pos = pos(), rotate: rot=rot(), name:str = None) -> None:
        super().__init__(name, pos, rotate)
        pass

class cobj(obj):
    def __init__(self, name:str = None, pos: pos = pos(), rot: rot=rot(), *args) -> None:
        super().__init__(name, pos, rot)
        self.l_obj = []
        for arg in args:
            self.add(arg)
        pass

    def add(self, a_obj) -> bool:
        if isinstance(a_obj, obj) or \
            isinstance(a_obj, dim.Dimensioning):
            self.l_obj.append(a_obj)
        else:
            raise Exception(f"Unallowed type {type(a_obj)}")
        return True

    def get(self) -> list:
        return self.l_obj

class aobj(cobj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), *args) -> None:
        super().__init__(name, pos, rot, *args)
        pass
class sobj(cobj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), *args) -> None:
        super().__init__(name, pos, rot, *args)
        pass
