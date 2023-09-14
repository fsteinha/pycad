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
                       a_pos:pos = pos(),
                       a_rot:rot = rot(),
                       name:str = "cube_angle_",
                       info: str = "",
                       purch:purch = None) -> None:
        """sobj for a travese whik is angled at the ends
            
          z ^                                                         z ^
            |                                                           |
            |                 /                                         |      
            |               y/                                          |      
            |               /                                           |            ____________.....
            |              /                                            |           |            |
            |             /                                             |           |            |
            |            /                                              |      -    |            |
            |           /                                               |           |            |  dx        y
            |          /                                                +-----------|            |------------->
            |         /  ____________________________...               /            |            |
            |        /  /                           / dy              /             |            |
            |       /  /___________________________/...              /              |____________|.....    
            |      /  :\                          /:                /              :\            /:
            |     /   : \                        / : dz            /               : \          / : 
            |    /    :  \                      /  :              /                :  \        /  : dz
            |   /     :   \                    /   :             /                 :   \      /   :
            |  /      :    \__________________/    :...         /                  :    \____/....:....
            | /       :-ax0:       dx         :-ax1:           /                   :-ay0: dy :-ay1:
            |/                                                /                    
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
        cube_angle = sobj(name=name, pos=a_pos, rot=a_rot,info=info, purch=purch)
        cube_angle.add(cube(dx,dy,dz))

        # proceed left side in xz layer
        #########################################################################
        if ax0 != 0:
          alx0 = math.tan(math.radians(abs(ax0))) * dz
          dlz0 = math.sqrt(alx0**2 + dz**2)
          dlx0 = alx0*math.cos(math.radians(abs(ax0)))
          dlx02 = dlx0*math.cos(math.radians(abs(ax0)))
          dlz02 = dlx0*math.sin(math.radians(abs(ax0)))
          print (dlz02)

          if (ax0 < 0):        
            cube_ang0 = cube(dlx0, dy, dlz0, rot=rot(0,ax0,0), pos=pos(alx0-dlx02,0,-dlz02))
            cube_angle.add(cube_ang0)
          elif (ax0 > 0):
            cube_ang0 = cube(dlx0, dy, dlz0, rot=rot(0,90-ax0,0), pos=pos(-(alx0-dlx02),0,dlz02))
            cube_angle.add(cube_ang0)
            
        # proceed right side in xz layer
        #########################################################################
        if ax1 != 0:
          alx1 = math.tan(math.radians(abs(ax1))) * dz
          dlz1 = math.sqrt(alx1**2 + dz**2)
          dlx1 = alx1*math.cos(math.radians(abs(ax1)))
          dlx12 = dlx0*math.cos(math.radians(abs(ax1)))
          dlz12 = dlx0*math.sin(math.radians(abs(ax1)))
          if (ax1 < 0):        
            #cube_ang1 = cube(dlx1, dy, dlz1, rot=rot(0,ax1,0), pos=pos(dx + (alx1-dlx12),0,dlz12))
            cube_ang1 = cube(dlx1, dy, dlz1, rot=rot(0,ax1,0), pos=pos(dx ,0,0))
            cube_angle.add(cube_ang1)
          elif (ax1 > 0):
            cube_ang1 = cube(dlx1, dy, dlz1, rot=rot(0,ax1,0), pos=pos(dx-(alx1),0,0))
            cube_angle.add(cube_ang1)
          
        
        return cube_angle
