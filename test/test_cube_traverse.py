import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse
from obj.constructives.mac_cube_traverse import *

# add addtional parmeters
##############################################################################

parser = prog_parse.prog_parse()
parser.add_argument("--dx", default=100, type=int, help="x dimension base cube")
parser.add_argument("--dy", default=100, type=int, help="y dimension base cube")
parser.add_argument("--dz", default=10, type=int, help="z dimension base cube")
parser.add_argument("--ax", default=100, type=int, help="left angle for miter in xz layer")
parser.add_argument("--ay", default=-100, type=int, help="right angle for miter in xz layer")
parser.add_argument("--bx", default=-0, type=int, help="left angle for miter in yz layer")
parser.add_argument("--by", default=-0, type=int, help="right angle for miter in yz layer")

args = parser.parse_args()

cube_traverse = mac_cube_traverse(args.dx,args.dy,args.dz,args.ax,args.ay, args.bx, args.by)

prog_parse.exam_execute([cube_traverse])

