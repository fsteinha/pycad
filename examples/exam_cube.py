import sys
sys.path.append("../src")

import pcad as pcad
import const_scad
import dimensioning as dim
import const_cadquery
import exam_parse

cube = pcad.aobj("cube_")
cube.add(pcad.cube(10, 10, 10))
cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(10,10,0),plane="yx",text="yx"))
cube.add(dim.Dimensioning(dim.Point(0,10,10),dim.Point(10,10,10),plane="yx",text="yx"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(10,0,0),plane="-yx",text="-yx"))
cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(10,0,10),plane="-yx",text="-yx"))
cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,10,0),plane="xy",text="xy"))
cube.add(dim.Dimensioning(dim.Point(10,0,10),dim.Point(10,10,10),plane="xy",text="xy"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,10,0),plane="-xy",text="-xy"))
cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(0,10,10),plane="-xy",text="-xy"))
cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(10,0,10),plane="zx",text="zx"))
cube.add(dim.Dimensioning(dim.Point(0,10,10),dim.Point(10,10,10),plane="zx",text="zx"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(10,0,0),plane="-zx",text="-zx"))
cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(10,10,0),plane="-zx",text="-zx"))
cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,0,10),plane="xz",text="xz"))
cube.add(dim.Dimensioning(dim.Point(10,10,0),dim.Point(10,10,10),plane="xz",text="xz"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,0,10),plane="-xz",text="-xz"))
cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(0,10,10),plane="-xz",text="-xz"))
cube.add(dim.Dimensioning(dim.Point(0,0,10),dim.Point(0,10,10),plane="zy",text="zy"))
cube.add(dim.Dimensioning(dim.Point(10,0,10),dim.Point(10,10,10),plane="zy",text="zy"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,10,0),plane="-zy",text="-zy"))
cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,10,0),plane="-zy",text="-zy"))
cube.add(dim.Dimensioning(dim.Point(0,10,0),dim.Point(0,10,10),plane="yz",text="yz"))
cube.add(dim.Dimensioning(dim.Point(10,10,0),dim.Point(10,10,10),plane="yz",text="yz"))
cube.add(dim.Dimensioning(dim.Point(10,0,0),dim.Point(10,0,10),plane="-yz",text="-yz"))
cube.add(dim.Dimensioning(dim.Point(0,0,0),dim.Point(0,0,10),plane="-yz",text="-yz"))

if exam_parse.M_SCAD==True:
    scad = const_scad.scad_const(exam_parse.get_const_name(__file__), cube)
    scad.show()
else:
    constcq = const_cadquery.cq_const(exam_parse.get_const_name(__file__), cube)
    constcq.show()
