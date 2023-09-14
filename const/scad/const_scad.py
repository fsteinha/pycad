import sys
sys.path.append("../../")

from pcad.pcad import *
from const.const import *
from const.scad.const_scad_aobj import aobj_const_scad
from const.scad.const_scad_sobj import sobj_const_scad
from const.scad.const_scad_dim import dim_const_scad
from const.scad.const_scad_cube import cube_const_scad
from const.scad.const_scad_cylinder import cylinder_const_scad
from const.scad.const_scad_sphere import sphere_const_scad

from obj.composites.obj_composite import aobj_const, sobj_const
from obj.dimension.obj_dim import dim_const
from obj.primitives.obj_cube import cube_const
from obj.primitives.obj_cylinder import cylinder_const
from obj.primitives.obj_sphere import sphere_const


import subprocess

class scad_const(const):
    def __init__(self, name, *l_obj) -> None:
        super().__init__(name, *l_obj)
        self.s_filename += ".scad"

        aobj_const().set_strategy(aobj_const_scad())
        sobj_const().set_strategy(sobj_const_scad())
        dim_const().set_strategy(dim_const_scad())
        cube_const().set_strategy(cube_const_scad())
        cylinder_c = cylinder_const()
        cylinder_c.set_strategy(cylinder_const_scad())
        test = cylinder_const()
        sphere_const().set_strategy(sphere_const_scad())

    def show(self, s_ecall="openscad"):
        self.iterate_obj(self.l_obj)
        f_file = open(self.s_filename, "w")
        f_file.write(self.s_out)
        f_file.close()
        print(f"{self.s_filename} created")
        s_call = f"{s_ecall} {self.s_filename}"
        print (s_call)
        p = subprocess.Popen([s_ecall, self.s_filename], stdout = subprocess.PIPE)
        print ("scad started")
        #p.wait()



