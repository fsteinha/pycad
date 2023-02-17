from pcad_obj import pobj
from pcad_pos import pos, rot

class cube(pobj):
    def __init__(self, dx:float=10.0, dy:float=10.0, dz:float=10.0, name = None, pos:pos=pos(), rot:rot=rot()) -> None:
        super().__init__(pos, rot, name)
        self.dx = dx
        self.dy = dy
        self.dz = dz
        
class cyclinder(pobj):
    def __init__(self,  drb:float=10.0, drt:float = 10.0, dh:float=10.0, name = None, pos:pos=pos(), rot:rot=rot()) -> None:
        super().__init__(pos, rot, name)
        self.drb = drb
        self.drt = drt
        self.dh  = dh
        
class sphere(pobj):
    def __init__(self, dr:float = 10.0, name = None, pos:pos=pos(), rot:rot=rot()) -> None:
        super().__init__(pos, rot, name)
        self.dr = dr
        
