import argparse
import re
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--m', choices=['scad', 'cq'], default='cq',
                    help='scad or cadquery')
args = parser.parse_args()

M_SCAD = False
M_CQ = False

match args.m:
    case 'scad':
        M_SCAD=True
    case other:
        M_CQ =True

def get_const_name(filename):
    return re.sub(r'\..+','',os.path.basename(filename))
