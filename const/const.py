""" base class for all constructors
"""
import sys
sys.path.append("../")

from pcad.pcad import *

class const:
    """base class for all constructors
    """
    def __init__(self, name:str, *l_obj) -> None:
        """_summary_

        Args:
            name (str): name of constructor (commes for inheritages)

        Raises:
            Exception: add method returns False
        """
        self.name = name
        self.s_out = ""
        self.l_obj = []
        self.s_filename = "pycad_" + name
        # check the objects
        for arg in l_obj:
            if type(arg) == list:
                for item in arg:
                    if self.add(item) == False:
                        raise Exception(f"Unallowed type  {type(item)} in list {arg}")
            else:
                if self.add(arg) == False:
                    raise Exception(f"Unallowed type {type(arg)}")

    def add(self, a_obj:obj) -> bool:
        """add the object to intern list

        Args:
            a_obj (obj): pcad object

        Returns:
            bool: True object can be added
                  False object can not be added
        """
        if isinstance(a_obj, obj) or isinstance(a_obj, Dimensioning):
            self.l_obj.append(a_obj)
        else:
            return False
        return True

    def add_const(self, a_obj:obj, a_const):
        """add a constructor callback function for the type of the given object

        Args:
            a_obj (obj): object
            a_const (_type_): constructor

        Raises:
            Exception: double definition of callers
        """
        if (type(a_obj) == self.d_const) and (a_const != self[type(a_obj)]):
            raise Exception (f"Double definition of caller {type(a_obj)}, {self[type(a_obj)]}, {a_const}")
        self.d_const[type(a_obj)] = a_const

    def iterate_obj(self, l_obj):
        for i_obj in l_obj:
            self.s_out += i_obj.const.proceed(i_obj)

    def show(self, ecall = None):
        raise Exception ("Function is virtual")


