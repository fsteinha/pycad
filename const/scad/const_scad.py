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
import psutil


class scad_const(const):
    def __init__(self, name, *l_obj) -> None:
        super().__init__(name, *l_obj)
        self.s_filename += ".scad"


    def set_strategy(self):
        aobj_const().set_strategy(aobj_const_scad())
        sobj_const().set_strategy(sobj_const_scad())
        dim_const().set_strategy(dim_const_scad())
        cube_const().set_strategy(cube_const_scad())
        cylinder_const().set_strategy(cylinder_const_scad())
        sphere_const().set_strategy(sphere_const_scad())

    def show(self, s_ecall="openscad"):
        self.set_strategy()
        self.iterate_obj(self.l_obj)
        f_file = open(self.s_filename, "w")
        f_file.write(self.s_out)
        f_file.close()
        print(f"{self.s_filename} created")
        if (self.is_process_running(s_ecall) == False):
            s_call = f"{s_ecall} {self.s_filename}"
            print (s_call)
            p = subprocess.Popen([s_ecall, self.s_filename], stdout = subprocess.PIPE)
            print ("scad started")
            #p.wait()

    def is_process_running(self, process_name):
        for process in psutil.process_iter(attrs=['name']):
            try:
                if process.info['name'] == process_name:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False




