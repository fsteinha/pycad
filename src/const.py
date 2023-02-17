from pcad_obj import *

class const:
    def __init__(self, name, *l_obj) -> None:
        self.name = name
        self.l_obj = []
        for arg in l_obj:
            if self.add(arg) == False:
                raise Exception(f"Unallowed type {type(arg)}")
            
    def add(self, a_obj) -> bool:
        if isinstance(a_obj, obj):
            self.l_obj.append(a_obj)
        else:
            return False
        return True
    
    def show(self):
        raise Exception ("Function is virtual")
