import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse
from obj.constructives.mac_cube_traverse import *

# add addtional parmeters
##############################################################################

parser = prog_parse.prog_parse()
parser.add_argument("--dx", default=10, type=int, help="x dimension base cube")
parser.add_argument("--dy", default=10, type=int, help="y dimension base cube")
parser.add_argument("--dz", default=10, type=int, help="z dimension base cube")
parser.add_argument("--a", default=100, type=int, help="left z-dimension")
parser.add_argument("--b", default=100, type=int, help="x/y dimension")
parser.add_argument("--c", default=0  , type=int, help="right z-dimension")
parser.add_argument("--yz_plane", default=False, action="store_true", help="right z-dimension")

args = parser.parse_args()
print(args)
if args.yz_plane == False:
    cube_traverse = mac_cube_traverse_xz(args.dy,args.dz,args.a, args.b, args.c)
else:
    cube_traverse = mac_cube_traverse_yz(args.dx,args.dz,args.a, args.b, args.c)

prog_parse.exam_execute([cube_traverse])

