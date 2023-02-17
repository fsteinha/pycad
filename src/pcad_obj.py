from pcad_pos import pos, rot
import traceback

class obj:
    def __init__(self, name:str = None, pos:pos=pos(),rot:rot=rot()) -> None:
        self.pos = pos
        self.rot = rot
        self.name = name
        print(__class__)
        pass
    
    def mov(self, mx=0, my=0, mz=0) -> None:
        self.pos.mov(mx, my, mz)
        pass

    def rot(self, ax=0, ay=0, az=0) -> None:
        self.rot.rot(ax, ay, az)        
        pass
    
    def set_name(self, name) -> None:
        self.name = name
        pass
    
    def get_name(self) -> str:
        if self.name == None:
            self.name = str(id(self))
            
        return self.name

class pobj(obj):
    def __init__(self, pos: pos = pos(), rotate: rot=rot(), name:str = None) -> None:
        super().__init__(name, pos, rotate)
        pass
    
class cobj(obj):
    def __init__(self, name:str = None, pos: pos = pos(), rot: rot=rot(), *args) -> None:
        super().__init__(name, pos, rot)
        self.l_obj = []
        for arg in args:
            if self.add(arg) == False:
                raise Exception(f"Unallowed type {type(arg)}")
        pass
    
    def add(self, a_obj) -> bool:
        if isinstance(a_obj, obj):
            self.l_obj.append(a_obj)
        else:
            return False
        return True
    
    def get(self) -> list:
        return self.l_obj

class sobj(cobj):
    def __init__(self, name:str = None, pos: pos = pos(), rot:rot=rot(), *args) -> None:
        super().__init__(name, pos, rot, *args)
        pass
