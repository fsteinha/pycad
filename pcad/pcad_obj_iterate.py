# helper function for
import pcad as pcad


def obj_iterate(l_obj, caller) -> None:
    for i_obj in l_obj:
        if isinstance(i_obj, pcad.cube):
            caller.cube(i_obj)
        elif isinstance(i_obj, pcad.cylinder):
            caller.cylinder(i_obj)
        elif isinstance(i_obj, pcad.aobj):
            caller.aobj(i_obj)
        elif isinstance(i_obj, pcad.dim.Dimensioning):
            caller.dim(i_obj)
        elif isinstance(i_obj, pcad.sobj):
            caller.sobj(i_obj)
        else:
            raise Exception (f"Unknown {type(i_obj)}")
