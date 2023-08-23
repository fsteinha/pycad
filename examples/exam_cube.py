import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse

cube = pcad.aobj("cube_")
cube.add(pcad.cube(10, 10, 10))
cube.add(pcad.Dimensioning(pcad.Point(0,10,0),pcad.Point(10,10,0),plane="yx",text="yx"))
cube.add(pcad.Dimensioning(pcad.Point(0,10,10),pcad.Point(10,10,10),plane="yx",text="yx"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(10,0,0),plane="-yx",text="-yx"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,10),pcad.Point(10,0,10),plane="-yx",text="-yx"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,0),pcad.Point(10,10,0),plane="xy",text="xy"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,10),pcad.Point(10,10,10),plane="xy",text="xy"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(0,10,0),plane="-xy",text="-xy"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,10),pcad.Point(0,10,10),plane="-xy",text="-xy"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,10),pcad.Point(10,0,10),plane="zx",text="zx"))
cube.add(pcad.Dimensioning(pcad.Point(0,10,10),pcad.Point(10,10,10),plane="zx",text="zx"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(10,0,0),plane="-zx",text="-zx"))
cube.add(pcad.Dimensioning(pcad.Point(0,10,0),pcad.Point(10,10,0),plane="-zx",text="-zx"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,0),pcad.Point(10,0,10),plane="xz",text="xz"))
cube.add(pcad.Dimensioning(pcad.Point(10,10,0),pcad.Point(10,10,10),plane="xz",text="xz"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(0,0,10),plane="-xz",text="-xz"))
cube.add(pcad.Dimensioning(pcad.Point(0,10,0),pcad.Point(0,10,10),plane="-xz",text="-xz"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,10),pcad.Point(0,10,10),plane="zy",text="zy"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,10),pcad.Point(10,10,10),plane="zy",text="zy"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(0,10,0),plane="-zy",text="-zy"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,0),pcad.Point(10,10,0),plane="-zy",text="-zy"))
cube.add(pcad.Dimensioning(pcad.Point(0,10,0),pcad.Point(0,10,10),plane="yz",text="yz"))
cube.add(pcad.Dimensioning(pcad.Point(10,10,0),pcad.Point(10,10,10),plane="yz",text="yz"))
cube.add(pcad.Dimensioning(pcad.Point(10,0,0),pcad.Point(10,0,10),plane="-yz",text="-yz"))
cube.add(pcad.Dimensioning(pcad.Point(0,0,0),pcad.Point(0,0,10),plane="-yz",text="-yz"))

prog_parse.exam_execute([cube])
