import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse
from obj.constructives.mac_cube_angle import *

cube_angle = mac_cube_angle_ab(100,10,10,45,-45)

prog_parse.exam_execute([cube_angle])

    