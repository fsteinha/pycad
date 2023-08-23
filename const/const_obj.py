"""base singleton classes for object constructors

    Returns:
        _type_: _description_
"""
import sys
sys.path.append("../")

from const.const_strat import const_strat_base

class const_obj_meta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class const_obj_base(metaclass=const_obj_meta):
    def __init__(self) -> None:
        self.strategy:const_strat_base = None
        pass

    def set_strategy(self, strategy:const_strat_base):
        self.strategy = strategy

    def proceed(self):
        self.strategy.proceed(self)

