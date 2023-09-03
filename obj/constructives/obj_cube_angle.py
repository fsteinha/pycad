import sys

sys.path.append("../../")


from pcad import *
from pcad.pcad_obj import pcad_obj, pcad_pos

from const import const_obj

class cube_angle_const(const_obj.const_obj_base):
    pass

class cube_angle():
    def __init__(self,
                 dx:float=10.0,
                 dy:float=10.0,
                 da:float=100.0,
                 db:float=100.0,
                 name: str = None,
                 pos:pcad_pos = pcad_pos.pos(),
                 rot:pcad_rot = pcad_pos.rot(),
                 info: str = "",
                 purch:purch = None) -> None:
        """sobj for a travese whik is angled at the ends
              ____                     |\
             |\   \                  ––| \
             \ \   \                  : \ \
              \ \   \                 :  \ \
               \ \   \                :   \ \
                \ \   \             da:    \ \
                 \ \   \              :     \ \
                  \ \ __\             :      \ \
                   \|___| dy          _.......\_\
                      dx               |  db  |
        Args:
            dx (float, optional): x dimension cube. Defaults to 10.0.
            dy (float, optional): y dimension cube. Defaults to 10.0.
            da (float, optional): a length traverse angle. Defaults to 100.0.
            db (float, optional): b lengrh traverse angle. Defaults to 100.0.
            name (str, optional): name of construnction part. Defaults to None.
            pos (pos, optional):  postion in construction space. Defaults to pos().
            rot (rot, optional):  rotation. Defaults to rot().
            info (str, optional): additonal information. Defaults to "".
            purch (purch, optional): purchchase informaton. Defaults to None.
        """
        super().__init__(pos, rot, name, info, purch)
        self.dx = dx
        self.dy = dy
        self.da = da
        self.db = db
