"""base singleton classes for object constructors

    Returns:
        _type_: _description_
"""
import sys
sys.path.append("../")

from pcad_types.singleton import singleton
from const.const_strat import const_strat_base
class const_obj_base(metaclass=singleton):
    def __init__(self) -> None:
        self.strategy:const_strat_base = None
        pass

    def set_strategy(self, strategy:const_strat_base):
        self.strategy = strategy

    def proceed(self, obj):
        return self.strategy.proceed(obj)

