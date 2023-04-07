import sys
sys.path.append("../src")

import pcad as pcad
import const_scad
import const_cadquery
import dimensioning as dim
import exam_parse


thickness = 6;

drawer_x = 340;
drawer_y = 355;
drawer_z = 75;

front_x = 380;
front_y = thickness;
front_z = 115;
front_z_offset = -15;

drawer = pcad.aobj("drawer")
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
                       "frontplate", pcad.pos(-1*((front_x-drawer_x)/2), drawer_y, front_z_offset)))

dim.Dimensioning.TEXT_SIZE = 10
drawer.add(dim.Dimensioning(dim.Point(-1*((front_x-drawer_x)/2),drawer_y + thickness,0),dim.Point(0,0,0),plane="-xy"))
drawer.add(dim.Dimensioning(dim.Point(0,drawer_y,0),dim.Point(0,0,0),plane="-xy"))

drawer.add(dim.Dimensioning(dim.Point(-1*((front_x-drawer_x)/2),drawer_y + thickness,0),dim.Point(-1*((front_x-drawer_x)/2) + front_x,drawer_y + thickness,0),plane="yx"))

if exam_parse.M_SCAD==True:
    scad = const_scad.scad_const(exam_parse.get_const_name(__file__), drawer)
    scad.show()
else:
    constcq = const_cadquery.cq_const(exam_parse.get_const_name(__file__), drawer)
    constcq.show()


