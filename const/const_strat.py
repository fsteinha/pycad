"""base singelton classes for object constructors

    Returns:
        _type_: _description_
"""

class const_strat_meta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class const_strat_base(metaclass=const_strat_meta):
    def proceed(self, obj) -> None:
        raise Exception ("virtual method inheritance missing")

