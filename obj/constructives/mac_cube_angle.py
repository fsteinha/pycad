import sys

sys.path.append("../../")


from pcad.pcad import *
import math as math


def mac_cube_angle_ab( dx:float=10.0,
                       dy:float=10.0,
                       dz:float=10.0,
                       ax0:float=0,
                       ax1:float=0,
                       ay0:float=0,
                       ay1:float=0,
                       pos:pos = pos(),
                       rot:rot = rot(),
                       info: str = "",
                       purch:purch = None) -> None:
        """sobj for a travese whik is angled at the ends
            
          z ^                                                        z ^
            |                                                          |
            |                /                                         |      
            |              y/                                          |      
            |              /                                           |            __________......
            |             /                                            |           |          |
            |            /                                             |           |          |
            |           /                                              |      -    |          |
            |          /                                               |           |          |  dx        y
            |         /                                                +-----------|          |------------->
            |        /  __________________________...                 /            |          |
            |       /  /                         / dy                /             |          |
            |      /  /_________________________/...                /              |__________|.....    
            |     /  :\                        /:                  /              :\          /:
            |    /   : \                      / : dz              /               : \        / : dz
            |   /    :  \                    /  :                /                :  \      /  :
            |  /     :   \__________________/   :...            /                 :   \____/...:....
            | /      :ax0:       dx         :ax1:              /                  :ay0: dy :ay1:
            |/         ->                    <-               /                    ->       <-
            +------------------------------------->         x/
                                                  x 
                                Args:
            dx (float, optional): x dimension cube. Defaults to 10.0.
            dz (float, optional): z dimension cube. Defaults to 10.0.
            da (float, optional): a length traverse angle. Defaults to 100.0.
            db (float, optional): b lengrh traverse angle. Defaults to 100.0.
            name (str, optional): name of construnction part. Defaults to None.
            pos (pos, optional):  postion in construction space. Defaults to pos().
            rot (rot, optional):  rotation. Defaults to rot().
            info (str, optional): additonal information. Defaults to "".
            purch (purch, optional): purchchase informaton. Defaults to None.
        """
        cube_angle = sobj(name=name, pos=pos, rot=rot,info=info, purch=purch)
        cube_angle.add(cube(dx,dy,dz))
        alx0 = math.tan(ax0) * dz
        cube_angle.add(cube(alx0, dy, dz, rot=rot(ax0,0,0))
        return cube_angle
