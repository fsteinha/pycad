import argparse
import re
import os
import sys
sys.path.append("../const")

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
    if M_SCAD==True:
        import const_scad
        scad = const_scad.scad_const(file_name, objs)
        scad.show()
    elif M_CQ==True:
        import const_cadquery
        constcq = const_cadquery.cq_const(file_name, objs)
        constcq.show()
    else:
        raise Exception ("Unknown option")

# parse arguments
##############################################################################
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--m', choices=['scad', 'cq'], default='cq',
                    help='scad or cadquery')
args = parser.parse_args()

M_SCAD = False
M_CQ = False

match args.m:
    case 'scad':
        M_SCAD=True
    case 'cq':
        M_CQ =True
    case other:
        M_SCAD =True
