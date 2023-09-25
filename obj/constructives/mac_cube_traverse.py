import sys
sys.path.append("../../")

from pcad.pcad import *
from obj.constructives.mac_cube_angle import *
import math as math

CUT_VERTICAL   = 0
CUT_HORIZONTAL = 1
CUT_VERTICAL_HORIZONTAL = 2


def mac_cube_traverse_xz(dy:float=10.0,
                         dz:float=10.0,
                         a:float=10.0,
                         b:float=10.0,
                         c:float=0,
                         cut = CUT_VERTICAL,
                         a_pos:pos = pos(),
                         a_rot:rot = rot(),
                         name:str = None,
                         info: str = "",
                         purch:purch = None) -> None:
    """

          z ^
            |                 y/  .
            |                 /  .
            |                /      /\ .
            |               /   .. /  \ .
            |              /    : |\   \ .
            |             /     : | \   \ .
            |            /      : |  \   \ .
            |           /       : \   \   \ .
            |          /        :  \   \   \ .
            |         /         :   \   \   \ . .
            |        /        a :    \   \   \ ....
            |       /           :     \   \  /|
            |      /            :      \   \/ |  dz
            |     /             :       \  |  |....
            |    /              :        \ | / .
            |   /               ..........\|/ . .
            |  /                :   b     : . dy
            | /                          .
            |/
            +--------------------------------------------->
                                                        x


          z ^
            |                 y/  .
            |                 /  .          .........
            |                /             /|      :
            |               /             / |      :
            |              /             /| |      :
            |             /             / | /      :
            |            /             /  |/       :
            |           /             /  /         :
            |          /             /  /          : c
            |         /             / ./           :
            |        /             /  /            :
            |       /             /  /             :
            |      /             /  /              :
            |     /             |  /               :
            |    /              | / .              :
            |   /               |/....................
            |  /                 :        b        :
            | /                          .
            |/
            +--------------------------------------------->
                                                         x
    Create a cube traversal object in the XZ plane.

    Args:
        dy (float, optional): The height of the cube. Defaults to 10.0.
        dz (float, optional): The depth of the cube. Defaults to 10.0.
        a (float, optional): The length of one side of the cube (a or c should be > 0). Defaults to 10.0.
        b (float, optional): The width of the cube. Defaults to 10.0.
        c (float, optional): An alternative length of one side of the cube (a or c should be > 0). Defaults to 0.
        cut (int, optional): The type of cut, either CUT_VERTICAL or CUT_HORIZONTAL. Defaults to CUT_VERTICAL.
        a_pos (pos, optional): The position of the cube. Defaults to pos().
        a_rot (rot, optional): The rotation of the cube. Defaults to rot().
        name (str, optional): A name for the cube traversal object. Defaults to None.
        info (str, optional): Additional information about the cube traversal object. Defaults to "".
        purch (purch, optional): Purchase information. Defaults to None.

    Returns:
        None
    """

    cube_traverse = None
    assert (b > 0), "b > 0"
    assert (a >= 0), "a >= 0"
    assert (c >= 0), "c >= 0"

    if (cut == CUT_VERTICAL):
        if (a > 0):
            angle_x = math.degrees(math.atan2(a,b))
            dx = math.sqrt(a**2 + b**2)
            dx2 = math.sqrt(dx**2-dz**2) 
            angle_x3 = math.degrees(math.asin(dz/dx))
            angle_x2 = angle_x-angle_x3          
            off_x = 0-math.sin(math.radians(angle_x2))*dz
            off_z = a-math.cos(math.radians(angle_x2))*dz
            cube_traverse = mac_cube_angle(dx,dy,dz,-angle_x2, angle_x2, a_rot=rot(0,angle_x2,0), a_pos=pos(off_x,0,off_z))        
        elif (c > 0):
            angle_x = math.degrees(math.atan2(c,b))
            dx = math.sqrt(c**2 + b**2)
            dx2 = math.sqrt(dx**2-dz**2) 
            angle_x3 = math.degrees(math.asin(dz/dx))
            angle_x2 = angle_x-angle_x3          
            off_x = 0
            off_z = a
            cube_traverse = mac_cube_angle(dx,dy,dz,angle_x2,-angle_x2, a_rot=rot(0,-1*angle_x2,0), a_pos=pos(off_x,0,off_z))

    cube_traverse.pos=pos(cube_traverse.pos.x + a_pos.x, cube_traverse.pos.y + a_pos.y, cube_traverse.pos.z + a_pos.z)
    return cube_traverse

def mac_cube_traverse_yz(dx:float=10.0,
                         dz:float=10.0,
                         a:float=10.0,
                         b:float=10.0,
                         c:float=0,
                         cut = CUT_VERTICAL,
                         a_pos:pos = pos(),
                         a_rot:rot = rot(),
                         name:str = None,
                         info: str = "",
                         purch:purch = None) -> None:
    """

          z ^
            |                 y/
            |                 /
            |                /      /\ .                          /|      :
            |               /   .. /  \ .                        / |      :
            |              /    : |\   \ .                      /| |      :
            |             /     : | \   \ .                    / | /      :
            |            /      : |  \   \ .                  /  |/       :
            |           /       : \   \   \ .                /  /         :
            |          /        :  \   \   \ .              /  /          : c
            |         /         :   \   \   \ . .          / ./           :
            |        /        a :    \   \   \ ....       /  /            :
            |       /           :     \   \  /|          /  /             :
            |      /            :      \   \/ |  dz     /  /              :
            |     /             :       \  |  |....    |  /               :
            |    /              :        \ | / .       | / .              :
            |   /               ..........\|/ . .      |/....................
            |  /                :   b     : . dy        :        b        :
            | /                          .
            |/
            +------------------------------------------------------------------->
                                                                              x


                                                                                 ^z
                                                                                 |
                                                                                 |
                          /\                                      /|      :      |                /x
                      .. /  \ .                                  / |      :      |               /
                      : |\   \ .                                /| |      :      |              /
                      : | \   \ .                              / | /      :      |             /
                      : |  \   \ .                            /  |/       :      |            /
                      : \   \   \ .                          /  /         :      |           /
                      :  \   \   \ .                        /  /          : c    |          /
                      :   \   \   \ . .                    / ./           :      |         /
                    a :    \   \   \ ....                 /  /            :      |        /
                      :     \   \  /|                    /  /             :      |       /
                      :      \   \/ |  dz               /  /              :      |      /
                      :       \  |  |....              |  /               :      |     /
                      :        \ | / .                 | / .              :      |    /
                      ..........\|/ . .                |/....................    |   /
                      :   b     : . dy                  :        b        :      |  /
                                       .                                         | /
                                                                                 |/
            <--------------------------------------------------------------------+
             y

     Create a cube traversal object in the YZ plane.

    Args:
        dx (float, optional): The width of the cube. Defaults to 10.0.
        dz (float, optional): The depth of the cube. Defaults to 10.0.
        a (float, optional): The height of one side of the cube (a or c should be > 0). Defaults to 10.0.
        b (float, optional): The length of the cube. Defaults to 10.0.
        c (float, optional): An alternative height of one side of the cube (a or c should be > 0). Defaults to 0.
        cut (int, optional): The type of cut, either CUT_VERTICAL or CUT_HORIZONTAL. Defaults to CUT_VERTICAL.
        a_pos (pos, optional): The position of the cube. Defaults to pos().
        a_rot (rot, optional): The rotation of the cube. Defaults to rot().
        name (str, optional): A name for the cube traversal object. Defaults to None.
        info (str, optional): Additional information about the cube traversal object. Defaults to "".
        purch (purch, optional): Purchase information. Defaults to None.

    Returns:
        None
    """

    cube_traverse = None
    assert (b > 0), "b > 0"
    assert (a >= 0), "a >= 0"
    assert (c >= 0), "c >= 0"

    if (cut == CUT_VERTICAL):
        if (c > 0):
            angle_y = math.degrees(math.atan2(c,b))
            dy = math.sqrt(c**2 + b**2)
            dy2= math.sqrt(dy**2-dz**2)
            angle_y3 = math.degrees(math.asin(dz/dy))
            angle_y2 = angle_y-angle_y3
            off_y = -math.sin(math.radians(angle_y2))*dz
            off_z = c-math.cos(math.radians(angle_y2))*dz            
            cube_traverse = mac_cube_angle(dx,dy2,dz,0,0,-angle_y2,angle_y2, a_rot=rot(-1*angle_y2,0,0), a_pos=pos(0,off_y,off_z))
        elif (a > 0):
            angle_y = math.degrees(math.atan2(a,b))
            dy = math.sqrt(a**2 + b**2)
            dy2= math.sqrt(dy**2-dz**2)
            angle_y3 = math.degrees(math.asin(dz/dy))
            angle_y2 = angle_y-angle_y3
            cube_traverse = mac_cube_angle(dx,dy2,dz,0,0,angle_y2,-angle_y2, a_rot=rot(angle_y2,0,0), a_pos=pos(0,0,0))

    cube_traverse.pos=pos(cube_traverse.pos.x + a_pos.x, cube_traverse.pos.y + a_pos.y, cube_traverse.pos.z + a_pos.z)

    return cube_traverse



