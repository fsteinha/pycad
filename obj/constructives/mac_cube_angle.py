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
                       name:str = None,
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

          if (ax0 < 0):
            cube_angx0 = cube(dlx0, dy, dlz0, rot=rot(0,ax0,0), pos=pos(alx0-dlx02,0,-dlz02))
            cube_angle.add(cube_angx0)
          elif (ax0 > 0):
            cube_angx0 = cube(dlx0, dy, dlz0, rot=rot(0,ax0,0), pos=pos(-dlx02,0,dlz02))
            cube_angle.add(cube_angx0)

        # proceed right side in xz layer
        #########################################################################
        if ax1 != 0:
          alx1 = math.tan(math.radians(abs(ax1))) * dz
          dlz1 = math.sqrt(alx1**2 + dz**2)
          dlx1 = alx1*math.cos(math.radians(abs(ax1)))
          #dlx12 = dlx1*math.cos(math.radians(abs(ax1)))
          #dlz12 = dlx1*math.sin(math.radians(abs(ax1)))

          if (ax1 < 0):
            cube_angx1 = cube(dlx1, dy, dlz1, rot=rot(0,-ax1,0), pos=pos(dx - alx1,0,0))
            cube_angle.add(cube_angx1)
          elif (ax1 > 0):
            cube_angx1 = cube(dlx1, dy, dlz1, rot=rot(0,-ax1,0), pos=pos(dx,0,0))
            cube_angle.add(cube_angx1)

        # proceed left side in yz layer
        #########################################################################
        if ay0 != 0:
          aly0 = math.tan(math.radians(abs(ay0))) * dz
          dlz0 = math.sqrt(aly0**2 + dz**2)
          dly0 = aly0*math.cos(math.radians(abs(ay0)))
          dly02 = dly0*math.cos(math.radians(abs(ay0)))
          dlz02 = dly0*math.sin(math.radians(abs(ay0)))

          if (ay0 < 0):
            cube_angy0 = cube(dx,dly0, dlz0, rot=rot(-ay0,0,0), pos=pos(0,aly0-dly02,-dlz02))
            cube_angle.add(cube_angy0)
          elif (ay0 > 0):
            cube_angy0 = cube(dx,dly0, dlz0, rot=rot(-ay0,00), pos=pos(0,-dly02,dlz02))
            cube_angle.add(cube_angy0)

        # proceed right side in yz layer
        #########################################################################
        if ay1 != 0:
          aly1 = math.tan(math.radians(abs(ay1))) * dz
          dlz1 = math.sqrt(aly1**2 + dz**2)
          dly1 = aly1*math.cos(math.radians(abs(ay1)))
          #dly12 = dly1*math.cos(math.radians(abs(ay1)))
          #dlz12 = dly1*math.sin(math.radians(abs(ay1)))

          if (ay1 < 0):
            cube_angy1 = cube(dx,dly1, dlz1, rot=rot(ay1,0,0), pos=pos(0,dy-aly1,0))
            cube_angle.add(cube_angy1)
          elif (ay1 > 0):
            cube_angy1 = cube(dx,dly1, dlz1, rot=rot(ay1,0, 0), pos=pos(0,dy,0))
            cube_angle.add(cube_angy1)

        return cube_angle
