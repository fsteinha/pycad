import sys
sys.path.append("../src")

import pcad as pcad
import const_scad as const
import dimensioning as dim

cube = pcad.cobj("cube_")
cube.add(pcad.cube(10, 10, 10))
cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(10,10,0),plane="xy"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(10,0,0),plane="-xy"))
cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,10,0),plane="yx"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,10,0),plane="-yx"))
scad = const.scad("test_", cube)
scad.show()
