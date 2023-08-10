import sys
sys.path.append("../src")

import pcad as pcad
import const_scad
import dimensioning as dim
#import const_cadquery
import exam_parse

HEIGH = 2500
WITDH = 1800
LENGTH = 2000

post_1 = pcad.aobj("post_1", info = "")
post_1.add(pcad.cube(120, 120, 2500))
# cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(10,10,0),plane="yx"))
# cube.add(dim.Dimensioning(dim.Point(0,10,10),dim.Point(10,10,10),plane="yx"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(10,0,0),plane="-yx"))
# cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(10,0,10),plane="-yx"))
# cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,10,0),plane="xy"))
# cube.add(dim.Dimensioning(dim.Point(10,0,10),dim.Point(10,10,10),plane="xy"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,10,0),plane="-xy"))
# cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(0,10,10),plane="-xy"))
# cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(10,0,10),plane="zx"))
# cube.add(dim.Dimensioning(dim.Point(0,10,10),dim.Point(10,10,10),plane="zx"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(10,0,0),plane="-zx"))
# cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(10,10,0),plane="-zx"))
# cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,0,10),plane="xz"))
# cube.add(dim.Dimensioning(dim.Point(10,10,0),dim.Point(10,10,10),plane="xz"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,0,10),plane="-xz"))
# cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(0,10,10),plane="-xz"))
# cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(0,10,10),plane="zy"))
# cube.add(dim.Dimensioning(dim.Point(10,0,10),dim.Point(10,10,10),plane="zy"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,10,0),plane="-zy"))
# cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,10,0),plane="-zy"))
# cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(0,10,10),plane="yz"))
# cube.add(dim.Dimensioning(dim.Point(10,10,0),dim.Point(10,10,10),plane="yz"))
# cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,0,10),plane="-yz"))
# cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,0,10),plane="-yz"))

if exam_parse.M_SCAD==True:
    scad = const_scad.scad_const(exam_parse.get_const_name(__file__), post_1)
    scad.show()
#else:
#    constcq = const_cadquery.cq_const(exam_parse.get_const_name(__file__), cube)
#    constcq.show()
