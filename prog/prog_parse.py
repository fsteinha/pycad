import argparse
import re
import os
import sys

sys.path.append("../")
from pcad_types.singleton import singleton

class prog_parse(metaclass=singleton):
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description='Process some integers.')
        # scad parameter
        self.parser.add_argument("--scad", nargs='?', const="openscad", help="activate scad with option program path")
        pass
    
    def parse_args(self): 
        return self.parser.parse_args()
    
    def add_argument(self, *args, **kwargs):
        return self.parser.add_argument(*args, **kwargs)


# global program dictionary
##############################################################################

# Functions
##############################################################################
def get_const_name(filename:str):
    """returns the filename without extion

    Args:
        filename (str): path to the file

    Returns:
        _type_: base name of the file
    """
    return re.sub(r'\..+','',os.path.basename(filename))

def exam_execute(objs:list, purch = False, file_name:str=sys.argv[0]):
    """execute function for proceeding the pycad as programm

    Args:
        objs (list): pcad objectlist
        purch (bool, optional): True make a purchase list. Defaults to False.
        file_name (str, optional): file name for the output file (scad). Defaults to None.

    Raises:
        Exception: output is not clear
    """
    args = parser.parse_args()

    d_prog_opt = {
        "SCAD": {
            "Enable":True,
            "PATH": "openscad",
        },
        "CQ": False,
    }

    # Get the values
    if args.scad:
        d_prog_opt["SCAD"]["Enable"] = True
        if args.scad is True:
            d_prog_opt["SCAD"]["PATH"] = "openscad"
        else:
            d_prog_opt["SCAD"]["PATH"] = args.scad.replace("/","\\")

    if file_name == None:
        file_name = get_const_name(__file__)
    if d_prog_opt["SCAD"]["Enable"] ==True:
        sys.path.append("../")
        import const.scad.const_scad as const_scad
        scad = const_scad.scad_const(file_name, objs)
        scad.show(d_prog_opt["SCAD"]["PATH"])
    elif d_prog_opt["CQ"]["Enable"]==True:
        import const_cadquery
        constcq = const_cadquery.cq_const(file_name, objs)
        constcq.show(d_prog_opt["CQ"]["PATH"])
    else:
        raise Exception ("Unknown option")

# parse arguments
##############################################################################
parser = prog_parse()
        