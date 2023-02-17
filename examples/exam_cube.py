import sys
sys.path.append("../src")

import pcad as pcad
import const_scad as const

cube = pcad.cube(pcad.pos(10, 10, 10))
scad = const.scad("test", cube)
scad.show()
