import sys
sys.path.append("../src")

import pcad as pcad
import dimensioning as dim
import exam_parse
import copy

VERSION_POST_120_Bar_42_4_verzinkt = 1
VERSION_POST_100_Bar_42_4_verzinkt = 2
VERSION_POST_100_Bar_42_4_edelstahl = 3


VERSION = VERSION_POST_100_Bar_42_4_verzinkt

DIM_ALL_Z = 2600
DIM_ALL_X = 1800
DIM_ALL_MID_Y = 1400
DIM_ALL_DIP_Y = 440
DIM_ALL_Y = DIM_ALL_MID_Y + DIM_ALL_DIP_Y

DIM_PULL_UP_BAR_X = DIM_ALL_X
DIM_PULL_UP_BAR_Z = 2500

DIM_DIP_Z = 1500

DIM_ALL_CARRIER_Z = 2000

# purchases
##############################################################################
purch_post_120 = pcad.purch(link="https://www.bauhaus.info/konstruktionsvollholz/konstruktionsvollholz-nsi/p/20113465?variantfallback=diff0-diff1",
                    price = 13.4,
                    price_type=pcad.price_type.PRICE_TYPE_DIM,
                    price_dim=DIM_ALL_Z/1000)


purch_post_100 = pcad.purch(link="https://www.bauhaus.info/konstruktionsvollholz/konstruktionsvollholz-nsi/p/20121574",
                    price = 9.4,
                    price_type=pcad.price_type.PRICE_TYPE_DIM,
                    price_dim=DIM_ALL_Z/1000)

purch_pull_up_bar_verzinkt = pcad.purch(link="https://www.prokilo.de",
                    price = 38.20,
                    price_type=pcad.price_type.PRICE_TYPE_PCS,
                    price_dim=None)

purch_pull_up_bar_edelstahl = pcad.purch(link="https://www.prokilo.de",
                    price = 46.30,
                    price_type=pcad.price_type.PRICE_TYPE_PCS,
                    price_dim=None)


# Settings
##############################################################################
if VERSION == VERSION_POST_120_Bar_42_4_verzinkt:
    print (f"VERSION={VERSION}, 120 mm post, bar 42,4 verzinkt")
    purch_post = purch_post_120
    purch_pull_up_bar = purch_pull_up_bar_verzinkt
    DIM_POST=120
    DIM_PULL_UP_BAR_DRB =42.4
    DIM_PULL_UP_BAR_DRT =42.4
    DIM_PULL_UP_BAR_THICK = 2.5
elif VERSION == VERSION_POST_100_Bar_42_4_verzinkt:
    print (f"VERSION={VERSION}, 100 mm post, bar 42,4  verzinkt")
    purch_post = purch_post_100
    purch_pull_up_bar = purch_pull_up_bar_verzinkt
    DIM_POST=100
    DIM_PULL_UP_BAR_DRB =42.4
    DIM_PULL_UP_BAR_DRT =42.4
    DIM_PULL_UP_BAR_THICK = 2.5
elif VERSION == VERSION_POST_100_Bar_42_4_edelstahl:
    print (f"VERSION={VERSION}, 100 mm post, bar 42,4  Edelstahl")
    purch_post = purch_post_100
    purch_pull_up_bar = purch_pull_up_bar_edelstahl
    DIM_POST=100
    DIM_PULL_UP_BAR_DRB =42.4
    DIM_PULL_UP_BAR_DRT =42.4
    DIM_PULL_UP_BAR_THICK = 2.0
else:
    raise Exception ("Unknown version")


purch_post_träger = pcad.purch(link="https://www.amazon.de/H-Pfostenanker-H-Anker-schwer-Pfostenanker-feuerverzinkt/dp/B07D9L13KQ/ref=sr_1_17?keywords=pfostentr%C3%A4ger+120x120&qid=1691686086&sr=8-17",
                               price = 9.99,
                               price_type=pcad.price_type.PRICE_TYPE_PCS)




# object list
l_objs = []
test_objs = []

# dimension properties
dim_prop=dim.Dimensioning_Prop(aux_line_lenght=100, line_offset=20, text_offset=20, text_size=50, line_thickness=5)
dim_prop_2=dim.Dimensioning_Prop(aux_line_lenght=200, line_offset=20, text_offset=20, text_size=50, line_thickness=5)

# central objects
##############################################################################

# Bars
##############
tpl_barpullup = pcad.sobj("bar_pull_up_verzinkt", purch=purch_pull_up_bar)
tpl_barpullup.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2, drt=DIM_PULL_UP_BAR_DRT/2, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_barpullup.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2-DIM_PULL_UP_BAR_THICK, drt=DIM_PULL_UP_BAR_DRT/2-DIM_PULL_UP_BAR_THICK, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_barpullup.set_color(pcad.RGBColor.DARK_GREY)

tpl_bardip = pcad.sobj("bar_dip_verzinkt", purch=purch_pull_up_bar)
tpl_bardip.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2, drt=DIM_PULL_UP_BAR_DRT/2, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_bardip.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2-DIM_PULL_UP_BAR_THICK, drt=DIM_PULL_UP_BAR_DRT/2-DIM_PULL_UP_BAR_THICK, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_bardip.set_color(pcad.RGBColor.DARK_GREY)

# Posts
###############

# left post front
tpl_PostLeftFront = pcad.sobj("post_left_front", info = "", purch=purch_post)
tpl_PostLeftFront.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_Z))
tpl_PostLeftFront.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(60,0,DIM_ALL_CARRIER_Z)))

tpl_PostLeftMiddleEnd = pcad.sobj("post_left_middle_end", info = "", purch=purch_post)
#tpl_PostLeftMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, DIM_DIP_Z + DIM_POST*2))
tpl_PostLeftMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_CARRIER_Z + DIM_POST*2))
tpl_PostLeftMiddleEnd.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(60,0,DIM_ALL_CARRIER_Z)))

# right post
tpl_PostRightFront = pcad.sobj("post_right_front", purch=purch_post)
tpl_PostRightFront.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_Z))
tpl_PostRightFront.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_ALL_CARRIER_Z)))

tpl_PostRightMiddleEnd = pcad.sobj("post_right_middle_end", purch=purch_post)
#tpl_PostRightMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, DIM_DIP_Z + DIM_POST*2))
tpl_PostRightMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_CARRIER_Z + DIM_POST*2))
tpl_PostRightMiddleEnd.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_ALL_CARRIER_Z)))


# left side
##############################################################################
post_left_front = copy.copy(tpl_PostLeftFront)
post_left_front.name = "post_left_front"
l_objs.append(post_left_front)

post_left_middle = copy.copy(tpl_PostLeftMiddleEnd)
post_left_middle.name = "post_left_middle"
post_left_middle.pos = pcad.pos(0, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
l_objs.append(post_left_middle)

post_left_end = copy.copy(tpl_PostLeftMiddleEnd)
post_left_end.name = "post_left_end"
post_left_end.pos = pcad.pos(0, DIM_ALL_Y, 0)
l_objs.append(post_left_end)

carrier_left = pcad.sobj("carrier_left", pos=pcad.pos(0, -DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_post)
carrier_left.add(pcad.cube(DIM_POST, DIM_ALL_Y + 3*DIM_POST, DIM_POST))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_POST,0)))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_left.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,DIM_ALL_Y+ DIM_POST, 0)))
carrier_left.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(0,DIM_ALL_Y/2, DIM_POST/2)))
carrier_left.set_color(pcad.RGBColor.RED)
l_objs.append(carrier_left)

dim_front_middle=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
l_objs.append(dim_front_middle)

dim_middle_end=dim.Dimensioning(dim.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),dim.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
l_objs.append(dim_middle_end)

dim_front_end=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop_2)
l_objs.append(dim_front_end)

dim_front_heigh=dim.Dimensioning(dim.Point(DIM_POST/2,0,0),dim.Point(DIM_POST/2,0,DIM_ALL_Z),plane="-yz",prop=dim_prop_2)
l_objs.append(dim_front_heigh)

dim_pull_up_heigh=dim.Dimensioning(dim.Point(DIM_POST/2,0,0),dim.Point(DIM_POST/2,0,DIM_PULL_UP_BAR_Z),plane="-yz",prop=dim_prop)
l_objs.append(dim_pull_up_heigh)

dim_dip_heigh=dim.Dimensioning(dim.Point(0,post_left_middle.pos.y+DIM_POST/2,0),dim.Point(0,post_left_middle.pos.y+DIM_POST/2,DIM_DIP_Z),plane="-yz",prop=dim_prop_2)
l_objs.append(dim_dip_heigh)

# right side
##############################################################################
tpl_PostRightFront = copy.copy(tpl_PostRightFront)
tpl_PostRightFront.name = "post_right_front"
tpl_PostRightFront.pos = pcad.pos(DIM_ALL_X-DIM_POST,0,0)
l_objs.append(tpl_PostRightFront)

post_right_middle = copy.copy(tpl_PostRightMiddleEnd)
post_right_middle.name = "post_right_middle"
post_right_middle.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
l_objs.append(post_right_middle)

post_right_end = copy.copy(tpl_PostRightMiddleEnd)
post_right_end.name = "post_right_end"
post_right_end.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y, 0)
l_objs.append(post_right_end)

carrier_right = pcad.sobj("carrier_right", pos=pcad.pos(DIM_ALL_X-DIM_POST, -DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_post)
carrier_right.add(pcad.cube(DIM_POST, DIM_ALL_Y + 3*DIM_POST, DIM_POST))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_POST,0)))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y+ DIM_POST, 0)))
carrier_right.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(0,DIM_ALL_Y/2, DIM_POST/2)))
carrier_right.set_color(pcad.RGBColor.RED)
l_objs.append(carrier_right)

dim_front_width=dim.Dimensioning(dim.Point(DIM_POST/2,DIM_POST/2,0),dim.Point(DIM_ALL_X-DIM_POST/2,DIM_POST/2,0),plane="-zx",prop=dim_prop)
l_objs.append(dim_front_width)

# middle
carrier_middle = pcad.sobj("carrier_middle", pos=pcad.pos(-DIM_POST, DIM_ALL_Y/2-DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_post)
carrier_middle.add(pcad.cube(DIM_ALL_X + 2*DIM_POST, DIM_POST, DIM_POST))
carrier_middle.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(DIM_POST, 0, 0)))
carrier_middle.set_color(pcad.RGBColor.RED)
l_objs.append(carrier_middle)

pull_up_bar = copy.copy(tpl_barpullup)
pull_up_bar.name = "pull_up_bar"
pull_up_bar.pos = pcad.pos(0, DIM_POST/2, DIM_PULL_UP_BAR_Z)
l_objs.append(pull_up_bar)

dip_bar_front = copy.copy(tpl_bardip)
dip_bar_front.name = "dip_bar_front"
dip_bar_front.pos = pcad.pos(0, DIM_ALL_MID_Y, DIM_DIP_Z)
l_objs.append(dip_bar_front)

dip_bar_end = copy.copy(tpl_bardip)
dip_bar_end.name = "dip_bar_end"
dip_bar_end.pos = pcad.pos(0, DIM_ALL_Y + DIM_POST/2, DIM_DIP_Z)
l_objs.append(dip_bar_end)

# Execute
##############################################################################
exam_parse.exam_execute(l_objs)
pcad.purch_report(l_objs,None)