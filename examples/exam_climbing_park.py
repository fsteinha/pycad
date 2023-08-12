import sys
sys.path.append("../src")

import pcad as pcad
import const_scad
import dimensioning as dim
#import const_cadquery
import exam_parse
import copy

DIM_ALL_Z = 2500
DIM_ALL_X = 1800
DIM_ALL_MID_Y = 1400
DIM_ALL_DIP_Y = 500
DIM_ALL_Y = DIM_ALL_MID_Y + DIM_ALL_DIP_Y

DIM_PULL_UP_BAR_X = DIM_ALL_X
DIM_PULL_UP_BAR_Z = 2000

DIM_DIP_Z = 1000

DIM_POST=120

# purchases
purch_post = pcad.purch(link="https://www.bauhaus.info/konstruktionsvollholz/konstruktionsvollholz-nsi/p/20113465?variantfallback=diff0-diff1",
                    price = 13.4,
                    price_type=pcad.price_type.PRICE_TYPE_DIM,
                    price_dim=DIM_ALL_Z)

purch_post_träger = pcad.purch(link="https://www.amazon.de/H-Pfostenanker-H-Anker-schwer-Pfostenanker-feuerverzinkt/dp/B07D9L13KQ/ref=sr_1_17?keywords=pfostentr%C3%A4ger+120x120&qid=1691686086&sr=8-17",
                               price = 9.99,
                               price_type=pcad.price_type.PRICE_TYPE_PCS)

purch_bar_1 = pcad.purch(link="",
                               price=0.0,
                               price_type=pcad.price_type.PRICE_TYPE_DIM,
                               price_dim=DIM_ALL_X)

# object list
objs = []
test_objs = []

# dimension properties
dim_prop=dim.Dimensioning_Prop(aux_line_lenght=100, line_offset=20, text_offset=20, text_size=50, line_thickness=5)
dim_prop_2=dim.Dimensioning_Prop(aux_line_lenght=200, line_offset=20, text_offset=20, text_size=50, line_thickness=5)

# central objects
##############################################################################
bar_1 = pcad.sobj("bar_1", purch=purch_bar_1)
bar_1.add(pcad.cylinder(drb=45/2, drt=45/2, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
bar_1.add(pcad.cylinder(drb=40/2, drt=40/2, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
bar_1.set_color(pcad.RGBColor.DARK_GREY)

# left post
post_left = pcad.sobj("post_left", info = "", purch=purch_post)
post_left.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_Z))
post_left.add(pcad.cube(60, DIM_POST, DIM_POST, pos=pcad.pos(60,0,DIM_ALL_Z-2*DIM_POST)))

# right post
post_right = pcad.sobj("post_right", purch=purch_post)
post_right.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_Z))
post_right.add(pcad.cube(60, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_ALL_Z-2*DIM_POST)))


# left side
##############################################################################
post_left_front = copy.copy(post_left)
post_left_front.name = "post_left_front"
objs.append(post_left_front)

post_left_middle = copy.copy(post_left)
post_left_middle.name = "post_left_middle"
post_left_middle.pos = pcad.pos(0, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
objs.append(post_left_middle)

post_left_end = copy.copy(post_left)
post_left_end.name = "post_left_end"
post_left_end.pos = pcad.pos(0, DIM_ALL_Y, 0)
objs.append(post_left_end)

carrier_left = pcad.sobj("carrier_left", pos=pcad.pos(0, -DIM_POST, DIM_ALL_Z-2*DIM_POST), purch=purch_post)
carrier_left.add(pcad.cube(DIM_POST, DIM_ALL_Y + 3*DIM_POST, DIM_POST))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_POST,0)))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_ALL_Y+ DIM_POST, 0)))
carrier_left.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(0,DIM_ALL_Y/2, DIM_POST/2)))
carrier_left.set_color(pcad.RGBColor.RED)
objs.append(carrier_left)

dim_front_middle=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
objs.append(dim_front_middle)

dim_middle_end=dim.Dimensioning(dim.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),dim.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
objs.append(dim_middle_end)

dim_front_end=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop_2)
objs.append(dim_front_end)

dim_front_heigh=dim.Dimensioning(dim.Point(DIM_POST/2,0,0),dim.Point(DIM_POST/2,0,DIM_ALL_Z),plane="-yz",prop=dim_prop_2)
objs.append(dim_front_heigh)

dim_dip_heigh=dim.Dimensioning(dim.Point(0,post_left_middle.pos.y+DIM_POST/2,0),dim.Point(0,post_left_middle.pos.y+DIM_POST/2,DIM_DIP_Z),plane="-yz",prop=dim_prop_2)
objs.append(dim_dip_heigh)

# right side
##############################################################################
post_right_front = copy.copy(post_right)
post_right_front.name = "post_right_front"
post_right_front.pos = pcad.pos(DIM_ALL_X-DIM_POST,0,0)
objs.append(post_right_front)

post_right_middle = copy.copy(post_right)
post_right_middle.name = "post_right_middle"
post_right_middle.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
objs.append(post_right_middle)

post_right_end = copy.copy(post_right)
post_right_end.name = "post_right_end"
post_right_end.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y, 0)
objs.append(post_right_end)

carrier_right = pcad.sobj("carrier_right", pos=pcad.pos(DIM_ALL_X-DIM_POST, -DIM_POST, DIM_ALL_Z-2*DIM_POST), purch=purch_post)
carrier_right.add(pcad.cube(DIM_POST, DIM_ALL_Y + 3*DIM_POST, DIM_POST))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_POST,0)))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y+ DIM_POST, 0)))
carrier_right.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(0,DIM_ALL_Y/2, DIM_POST/2)))
carrier_right.set_color(pcad.RGBColor.RED)
objs.append(carrier_right)

dim_front_width=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_ALL_X-DIM_POST/2,DIM_POST/2,0),plane="-zx",prop=dim_prop)
objs.append(dim_front_width)

# middle
carrier_middle = pcad.sobj("carrier_middle", pos=pcad.pos(-DIM_POST, DIM_ALL_Y/2-DIM_POST, DIM_ALL_Z-2*DIM_POST), purch=purch_post)
carrier_middle.add(pcad.cube(DIM_ALL_X + 2*DIM_POST, DIM_POST, DIM_POST))
carrier_middle.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(DIM_POST, 0, 0)))
carrier_middle.set_color(pcad.RGBColor.RED)
objs.append(carrier_middle)

pull_up_bar = copy.copy(bar_1)
pull_up_bar.name = "pull_up_bar"
pull_up_bar.pos = pcad.pos(0, DIM_POST/2, DIM_PULL_UP_BAR_Z)
objs.append(pull_up_bar)

dip_bar_front = copy.copy(bar_1)
dip_bar_front.name = "dip_bar_front"
dip_bar_front.pos = pcad.pos(0, DIM_ALL_MID_Y, DIM_DIP_Z)
objs.append(dip_bar_front)

dip_bar_end = copy.copy(bar_1)
dip_bar_end.name = "dip_bar_end"
dip_bar_end.pos = pcad.pos(0, DIM_ALL_Y + DIM_POST/2, DIM_DIP_Z)
objs.append(dip_bar_end)

if exam_parse.M_SCAD==True:
    scad = const_scad.scad_const(exam_parse.get_const_name(__file__), objs)
    #scad = const_scad.scad_const(exam_parse.get_const_name(__file__), test_objs)
    scad.show()
#else:
#    constcq = const_cadquery.cq_const(exam_parse.get_const_name(__file__), cube)
#    constcq.show()
