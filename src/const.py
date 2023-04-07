from pcad_obj import *
from pcad_obj import *
from pcad_primitives import *

class const:
    def __init__(self, name, *l_obj) -> None:
        self.name = name
        self.l_obj = []
        self.s_filename = "pycad_" + name
        for arg in l_obj:
            if self.add(arg) == False:
                raise Exception(f"Unallowed type {type(arg)}")

    def add(self, a_obj) -> bool:
        if isinstance(a_obj, obj):
            self.l_obj.append(a_obj)
        else:
            return False
        return True

    def iterate_obj(self, l_obj):
        for i_obj in l_obj:
            if isinstance(i_obj, cube):
                self.cube(i_obj)
            elif isinstance(i_obj, aobj):
                self.aobj(i_obj)
            elif isinstance(i_obj, dim.Dimensioning):
                self.dim(i_obj)
            elif isinstance(i_obj, sobj):
                self.sobj(i_obj)
            else:
                raise Exception (f"Unknown {type(i_obj)}")

    def show(self):
        raise Exception ("Function is virtual")

    def cube(self):
        raise Exception ("Function is virtual")

    def aobj(self):
        raise Exception ("Function is virtual")

    def dim(self):
        raise Exception ("Function is virtual")

    def sobj(self):
        raise Exception ("Function is virtual")
