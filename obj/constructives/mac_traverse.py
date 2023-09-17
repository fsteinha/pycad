import sys
sys.path.append("../../")

from pcad.pcad import *
import math as math


def mac_angle_ab(dx:float=10.0,
                 dy:float=10.0,
                 dz:float=10.0,
                 ax:float=10.0,
                 bx:float=10.0,
                 ay:float=10.0,
                 by:float=10.0,
                 a_pos:pos = pos(),
                 a_rot:rot = rot(),
                 name:str = None,
                 info: str = "",
                 purch:purch = None) -> None:
    """

          z ^                                                         z ^
            |                 y/  .                                     |              .
            |                 /  .                                      |             .
            |                / /\ .                                     |           /\ .
            |               / /  \ .                                    |          /  \ .
            |              / |\   \ .                                   |         |\   \ .
            |             /  | \   \ . dx                               |         | \   \ . dy
            |            / ..|  \   \ .                                 |         |  \   \ .
            |           /    \   \   \ .                                |     ....\   \   \ .                y
            |          /     :\   \   \ .                               +------:---\   \   \-.---------------->
            |         /      : \   \   \ . .                           /       :    \   \   \ . .
            |        /    ax :  \   \   \ ....                        /        :     \   \   \ ....
            |       /        :   \   \  /|                           /       ay:      \   \  /|
            |      /         :    \   \/ |  dz                      /          :       \   \/ |  dz
            |     /          :     \  |  |....                     /           :        \  |  |....
            |    /           :      \ | / .                       /            :         \ | /.
            |   /          ..........\|/ . .                     /            .............|/.  .
            |  /             :   bx   : . dy                    /              :    by     :.  dx
            | /                          .                     /                             .
            |/                                                /
            +------------------------------------->         x/


    Args:
        dx (float, optional): _description_. Defaults to 10.0.
        dy (float, optional): _description_. Defaults to 10.0.
        dz (float, optional): _description_. Defaults to 10.0.
        ax (float, optional): _description_. Defaults to 10.0.
        bx (float, optional): _description_. Defaults to 10.0.
        ay (float, optional): _description_. Defaults to 10.0.
        by (float, optional): _description_. Defaults to 10.0.
        a_pos (pos, optional): _description_. Defaults to pos().
        a_rot (rot, optional): _description_. Defaults to rot().
        name (str, optional): _description_. Defaults to None.
        info (str, optional): _description_. Defaults to "".
        purch (purch, optional): _description_. Defaults to None.
    """

    cube_traverse = sobj(name=name, pos=a_pos, rot=a_rot,info=info, purch=purch)
    cube_base = cube(dx,dy,dz)
    cube_traverse.add(cube_base)

    if (ax != 0) and (ay != 0):
        angle = math.tan(ax/ay)
        cube_base.rot = rot(0,angle,0)


        pass

    return cube_traverse




