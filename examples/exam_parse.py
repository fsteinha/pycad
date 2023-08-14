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

def exam_execute(objs, purch = False):
    if M_SCAD==True:
        import const_scad
        scad = const_scad.scad_const(get_const_name(__file__), objs)
        scad.show()
    elif M_CQ==True:
        import const_cadquery
        constcq = const_cadquery.cq_const(get_const_name(__file__), objs)
        constcq.show()
    else:
        raise Exception ("Unknown option")

