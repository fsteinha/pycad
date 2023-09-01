import sys
sys.path.append("../")
from pcad.pcad_pos import pos, rot
from pcad.pcad_color import RGBColor
from purch.purch import purch
import gc


class obj:
    def __init__(self, name:str = None, pos:pos=pos(),rot:rot=rot(), color:RGBColor = RGBColor(), info:str="", purch:purch=None) -> None:
        self.pos = pos
        self.rot = rot
        self.set_name(name)
        self.set_color(color)
        self.info = []
        self.add_info(info)
        self.purch = purch
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
        if self.name == None:
            self.set_name(None)
        return self.name

    def set_color(self,color):
        if (color in RGBColor.COLORS):
            self.color = RGBColor(color)
        elif (isinstance(color, RGBColor)):
            self.color = color
        else:
            raise Exception(f"Not RGBColor object or an color setting {type(color)}")

    def add_info(self, info:str) -> None:
        self.info.append(info)







