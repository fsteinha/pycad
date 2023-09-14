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


# global program dictionary
##############################################################################
D_PROG_OPTIONS = {
    "SCAD": {
        "Enable":True,
        "PATH": "openscad",
    },
    "CQ": False,
}

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
    if file_name == None:
        file_name = get_const_name(__file__)
    if D_PROG_OPTIONS["SCAD"]["Enable"] ==True:
        sys.path.append("../")
        import const.scad.const_scad as const_scad
        scad = const_scad.scad_const(file_name, objs)
        scad.show(D_PROG_OPTIONS["SCAD"]["PATH"])
    elif D_PROG_OPTIONS["CQ"]["Enable"]==True:
        import const_cadquery
        constcq = const_cadquery.cq_const(file_name, objs)
        constcq.show(D_PROG_OPTIONS["CQ"]["PATH"])
    else:
        raise Exception ("Unknown option")

# parse arguments
##############################################################################
parser = prog_parse()
args = parser.parse_args()

# Get the values
if args.scad:
    D_PROG_OPTIONS["SCAD"]["Enable"] = True
    if args.scad is True:
        D_PROG_OPTIONS["SCAD"]["PATH"] = "openscad"
    else:
        D_PROG_OPTIONS["SCAD"]["PATH"] = args.scad.replace("/","\\")
        