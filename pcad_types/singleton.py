"""base singleton classes for object constructors

    Returns:
        _type_: _description_
"""
import sys
sys.path.append("../")

class singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
