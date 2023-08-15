import sys
sys.path.append("../pcad")

import pcad as pcad
import pcad_dim as dim
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

exam_parse.exam_execute([cube])
