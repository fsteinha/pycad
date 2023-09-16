import sys
sys.path.append("../")

import pcad.pcad as pcad
import obj.dimension.obj_dim as dim
import prog.prog_parse as prog_parse


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

prog_parse.exam_execute([drawer])