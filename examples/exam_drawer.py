import sys
sys.path.append("../src")

import pcad as pcad
import const_scad as const


thickness = 6;

drawer_x = 340;
drawer_y = 355;
drawer_z = 75;

front_x = 380;
front_y = thickness;
front_z = 125;

drawer = pcad.cobj("drawer")
drawer.add(pcad.cube(drawer_x - 2* thickness, thickness, drawer_z,
                       "backside", pcad.pos(thickness, 0,0)))
drawer.add(pcad.cube(drawer_x - 2* thickness, thickness, drawer_z,
                       "frontside", pcad.pos(thickness, drawer_y-thickness,0)))
drawer.add(pcad.cube(thickness, drawer_y, drawer_z,
                       "leftside", pcad.pos(drawer_x - thickness, 0,0)))
drawer.add(pcad.cube(thickness, drawer_y, drawer_z,
                       "righside"))
drawer.add(pcad.cube(drawer_x - 2*thickness, drawer_y - 2*thickness, thickness, 
                       "bottom", pcad.pos(thickness, thickness, 0)))
drawer.add(pcad.cube(front_x, thickness, front_z, 
                       "frontplate", pcad.pos(-1*((front_x-drawer_x)/2), drawer_y, -1*(front_z-drawer_z))))


scad = const.scad("test", drawer)
scad.show()
