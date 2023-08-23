from pcad_primitives import *
from pcad_obj import *
from pcad_pos import pos, rot
from pcad_purch import purch

class traverse_angle(pobj):
    def __init__(self,
                 dx:float=10.0,
                 dy:float=10.0,
                 da:float=100.0,
                 db:float=100.0,
                 name: str = None,
                 pos: pos = pos(),
                 rot: rot = rot(),
                 info: str = "",
                 purch: purch = None) -> None:
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
