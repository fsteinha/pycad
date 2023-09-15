import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse
from obj.constructives.mac_cube_angle import *

# add addtional parmeters
##############################################################################

parser = prog_parse.prog_parse()
parser.add_argument("--dx", default=100, type=int, help="x dimension base cube")
parser.add_argument("--dy", default=100, type=int, help="y dimension base cube")
parser.add_argument("--dz", default=10, type=int, help="z dimension base cube")
parser.add_argument("--ax0", default=0, type=int, help="left angle for miter in xz layer")
parser.add_argument("--ax1", default=0, type=int, help="right angle for miter in xz layer")
parser.add_argument("--ay0", default=45, type=int, help="left angle for miter in yz layer")
parser.add_argument("--ay1", default=-45, type=int, help="right angle for miter in yz layer")

args = parser.parse_args()

cube_angle = mac_cube_angle_ab(args.dx,args.dy,args.dz,args.ax0,args.ax1, args.ay0, args.ay1)

prog_parse.exam_execute([cube_angle])

    