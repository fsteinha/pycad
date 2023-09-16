"""base singelton classes for object constructors

    Returns:
        _type_: _description_
"""
from pcad_types.singleton import singleton
class const_strat_base(metaclass=singleton):
    def proceed(self, obj) -> None:
        raise Exception ("virtual method inheritance missing")

