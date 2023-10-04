import sys
sys.path.append("../")

import pcad.pcad as pcad
import prog.prog_parse as prog_parse
from obj.constructives.mac_cube_traverse import *

DIM_ALL_Z = 3000
DIM_ALL_X = 1800
DIM_ALL_MID_Y = 1600
DIM_ALL_DIP_Y = 450
DIM_ALL_Y = DIM_ALL_MID_Y + DIM_ALL_DIP_Y

DIM_MID_Z = 2400

DIM_PULL_UP_BAR_X = DIM_ALL_X
DIM_PULL_UP_BAR_Z = 2500

DIM_DIP_Z = 1500

DIM_ALL_CARRIER_Z = 2200

DIM_TRAVERSE_Z = 300
DIM_TRAVERSE_X = DIM_TRAVERSE_Z
DIM_TRAVERSE_Y = DIM_TRAVERSE_X

# purchases
##############################################################################
purch_post_100 = pcad.purch(link="https://www.bauhaus.info/konstruktionsvollholz/konstruktionsvollholz-nsi/p/20121574",
                    price = 9.4,
                    price_type=pcad.price_type.PRICE_TYPE_DIM,
                    price_dim=DIM_ALL_Z/1000)

purch_post_100_2_4 = pcad.purch(link="https://www.possling.de/preisliste/Bau-_und_Tischlerholz_rau%7Cgehobelt/Konstruktionsholz/Brettschichtholz_%7C_Leimbinder_BSH/Brettschichtholz%2C_Fichte/katalog/530359/galerie/1/artikel.php",
                     info="Holzpossling, Leimbinder Fichte 2.4 m,Bestell-Nr.: 530359",
                     price = 26.28,
                     price_type=pcad.price_type.PRICE_TYPE_PCS)

purch_post_100_3 = pcad.purch(link="",
                   info="Holzpossling, Leimbinder Fichte 3 m",
                   price = 32.85,
                   price_type=pcad.price_type.PRICE_TYPE_PCS)

purch_carrier = pcad.purch(link="",
                   info="Holzpossling, Leimbinder Fichte 70x95 m",
                   price = 17,
                   price_type=pcad.price_type.PRICE_TYPE_PCS)

purch_pull_up_bar_verzinkt = pcad.purch(link="https://www.prokilo.de",
                    price = 38.20,
                    price_type=pcad.price_type.PRICE_TYPE_PCS,
                    price_dim=None)

purch_post_ancor = pcad.purch(link="https://www.amazon.de/H-Pfostenanker-H-Anker-schwer-Pfostenanker-feuerverzinkt/dp/B07D9L13KQ/ref=sr_1_17?keywords=pfostentr%C3%A4ger+120x120&qid=1691686086&sr=8-17",
                               price = 9.99,
                               price_type=pcad.price_type.PRICE_TYPE_PCS)


# Settings
##############################################################################
print (f"VERSION: 100 mm post, bar 42,4  verzinkt")
purch_pull_up_bar = purch_pull_up_bar_verzinkt
DIM_POST=100
DIM_PULL_UP_BAR_DRB =42.4
DIM_PULL_UP_BAR_DRT =42.4
DIM_PULL_UP_BAR_THICK = 2.5

DIM_CARRIER_X = 70
DIM_CARRIER_Z = 95

DIM_CARRIER_NOTCH_X = 20
DIM_CARRIER_NOTCH_Z = DIM_CARRIER_Z

# object list
l_objs = []
test_objs = []

# dimension properties
dim_prop=pcad.Dimensioning_Prop(aux_line_lenght=100, line_offset=20, text_offset=20, text_size=50, line_thickness=5)
dim_prop_2=pcad.Dimensioning_Prop(aux_line_lenght=200, line_offset=20, text_offset=20, text_size=50, line_thickness=5)

# central objects
##############################################################################

# Bars
##############
tpl_barpullup = pcad.sobj("bar_pull_up_verzinkt", purch=purch_pull_up_bar)
tpl_barpullup_dz = DIM_ALL_X
tpl_barpullup.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2, drt=DIM_PULL_UP_BAR_DRT/2, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_barpullup.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2-DIM_PULL_UP_BAR_THICK, drt=DIM_PULL_UP_BAR_DRT/2-DIM_PULL_UP_BAR_THICK, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_barpullup.purch.price_dim=tpl_barpullup_dz/1000
tpl_barpullup.set_color(pcad.RGBColor.DARK_GREY)

tpl_bardip = pcad.sobj("bar_dip_verzinkt", purch=purch_pull_up_bar)
tpl_bardip_dz = DIM_ALL_X
tpl_bardip.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2, drt=DIM_PULL_UP_BAR_DRT/2, dh=tpl_bardip_dz, rot=pcad.rot(ay=90)))
tpl_bardip.add(pcad.cylinder(drb=DIM_PULL_UP_BAR_DRB/2-DIM_PULL_UP_BAR_THICK, drt=DIM_PULL_UP_BAR_DRT/2-DIM_PULL_UP_BAR_THICK, dh=DIM_ALL_X, rot=pcad.rot(ay=90)))
tpl_bardip.set_color(pcad.RGBColor.DARK_GREY)

# Posts
###############

# left post front
tpl_PostLeftFront = pcad.sobj("post_left_front", info = "", purch=purch_post_100_3)
tpl_PostLeftFront_dz = DIM_ALL_Z
tpl_PostLeftFront.add(pcad.cube(DIM_POST, DIM_POST, tpl_PostLeftFront_dz))
tpl_PostLeftFront.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(60,0,DIM_ALL_CARRIER_Z)))

tpl_PostLeftMiddleEnd = pcad.sobj("post_left_middle_end", info = "", purch=purch_post_100_2_4)
tpl_PostLeftMiddleEnd_z = DIM_MID_Z
tpl_PostLeftMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, tpl_PostLeftMiddleEnd_z))
tpl_PostLeftMiddleEnd.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(60,0,DIM_ALL_CARRIER_Z)))

# right post
tpl_PostRightFront = pcad.sobj("post_right_front", purch=purch_post_100_3)
tpl_PostRightFront_dz = DIM_ALL_Z
tpl_PostRightFront.add(pcad.cube(DIM_POST, DIM_POST, DIM_ALL_Z))
tpl_PostRightFront.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_ALL_CARRIER_Z)))

tpl_PostRightMiddleEnd = pcad.sobj("post_right_middle_end", purch=purch_post_100_2_4)
tpl_PostRightMiddleEnd_dz = DIM_MID_Z
tpl_PostRightMiddleEnd.add(pcad.cube(DIM_POST, DIM_POST, tpl_PostRightMiddleEnd_dz))
tpl_PostRightMiddleEnd.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_ALL_CARRIER_Z)))

# left side
##############################################################################
post_left_front = tpl_PostLeftFront.copy()
post_left_front.name = "post_left_front"
l_objs.append(post_left_front)

post_left_middle = tpl_PostLeftMiddleEnd.copy()
post_left_middle.name = "post_left_middle"
post_left_middle.pos = pcad.pos(0, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
l_objs.append(post_left_middle)

post_left_end = tpl_PostLeftMiddleEnd.copy()
post_left_end.name = "post_left_end"
post_left_end.pos = pcad.pos(0, DIM_ALL_Y, 0)
l_objs.append(post_left_end)

carrier_left = pcad.sobj("carrier_left", pos=pcad.pos(DIM_POST-DIM_CARRIER_X, -DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_carrier)
carrier_left_lenght = DIM_ALL_Y + 3*DIM_POST
carrier_left.add(pcad.cube(DIM_CARRIER_X, carrier_left_lenght, DIM_CARRIER_Z))
carrier_left.add(pcad.cube(DIM_CARRIER_NOTCH_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(0,DIM_POST,0)))
carrier_left.add(pcad.cube(DIM_CARRIER_NOTCH_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(0,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_left.add(pcad.cube(DIM_CARRIER_NOTCH_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(0,DIM_ALL_Y+ DIM_POST, 0)))
carrier_left.set_color(pcad.RGBColor.RED)
l_objs.append(carrier_left)

traverse_angle_left = mac_cube_traverse_yz(DIM_POST,DIM_POST,0, DIM_TRAVERSE_Y, DIM_TRAVERSE_Z, a_pos=pos(0,DIM_POST,0), purch=purch_post_100_2_4)
traverse_angle_left.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_angle_left)


dim_front_middle=pcad.Dimensioning(pcad.Point(DIM_POST/2,DIM_POST/2,0),pcad.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
l_objs.append(dim_front_middle)

dim_middle_end=pcad.Dimensioning(pcad.Point(DIM_POST/2,post_left_middle.pos.y+DIM_POST/2,0),pcad.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop)
l_objs.append(dim_middle_end)

dim_front_end=pcad.Dimensioning(pcad.Point(DIM_POST/2,DIM_POST/2,0),pcad.Point(DIM_POST/2,DIM_ALL_Y+DIM_POST/2,0),plane="-zy",prop=dim_prop_2)
l_objs.append(dim_front_end)

dim_front_heigh=pcad.Dimensioning(pcad.Point(DIM_POST/2,0,0),pcad.Point(DIM_POST/2,0,DIM_ALL_Z),plane="-yz",prop=dim_prop_2)
l_objs.append(dim_front_heigh)

dim_pull_up_heigh=pcad.Dimensioning(pcad.Point(DIM_POST/2,0,0),pcad.Point(DIM_POST/2,0,DIM_PULL_UP_BAR_Z),plane="-yz",prop=dim_prop)
l_objs.append(dim_pull_up_heigh)

dim_dip_heigh=pcad.Dimensioning(pcad.Point(0,post_left_middle.pos.y+DIM_POST/2,0),pcad.Point(0,post_left_middle.pos.y+DIM_POST/2,DIM_DIP_Z),plane="-yz",prop=dim_prop_2)
l_objs.append(dim_dip_heigh)

l_objs.append(dim_dip_heigh)

# right side
##############################################################################
post_PostRightFront = tpl_PostRightFront.copy()
post_PostRightFront.name = "post_right_front"
post_PostRightFront.pos = pcad.pos(DIM_ALL_X-DIM_POST,0,0)
l_objs.append(post_PostRightFront)

post_right_middle = tpl_PostRightMiddleEnd.copy()
#post_right_middle.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(0,0,DIM_TRAVERSE_Z)))
post_right_middle.name = "post_right_middle"
post_right_middle.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y - DIM_POST/2 - DIM_ALL_DIP_Y, 0)
l_objs.append(post_right_middle)

post_right_end = tpl_PostRightMiddleEnd.copy()
post_right_end.name = "post_right_end"
post_right_end.pos = pcad.pos(DIM_ALL_X-DIM_POST, DIM_ALL_Y, 0)
l_objs.append(post_right_end)

carrier_right = pcad.sobj("carrier_right", pos=pcad.pos(DIM_ALL_X-DIM_POST, -DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_carrier)
carrier_right_lenght = DIM_ALL_Y + 3*DIM_POST
carrier_right.add(pcad.cube(DIM_CARRIER_X, carrier_right_lenght, DIM_CARRIER_Z))
carrier_right.add(pcad.cube(DIM_CARRIER_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(DIM_POST/2,DIM_POST,0)))
carrier_right.add(pcad.cube(DIM_CARRIER_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y + DIM_POST/2 - DIM_ALL_DIP_Y, 0)))
carrier_right.add(pcad.cube(DIM_CARRIER_X, DIM_POST, DIM_CARRIER_Z, pos=pcad.pos(DIM_POST/2,DIM_ALL_Y+ DIM_POST, 0)))
#carrier_right.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(0,DIM_ALL_Y/2, DIM_POST/2)))
carrier_right.set_color(pcad.RGBColor.RED)
carrier_right.purch.price_dim=carrier_right_lenght/1000
l_objs.append(carrier_right)

#traverse_straigth_right = pcad.sobj("traverse_straigth_right", pos=pos(DIM_ALL_X-DIM_POST,0, DIM_TRAVERSE_Z), purch=purch_post)
#traverse_straigth_right.add(pcad.cube(DIM_POST, post_left_middle.pos.y + DIM_POST, DIM_POST))
#traverse_straigth_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,0,0)))
#traverse_straigth_right.add(pcad.cube(DIM_POST/2, DIM_POST, DIM_POST, pos=pcad.pos(DIM_POST/2,post_left_middle.pos.y,0)))
#traverse_straigth_right.set_color(pcad.RGBColor.RED)
#l_objs.append(traverse_straigth_right)

traverse_angle_right = mac_cube_traverse_yz(DIM_POST,DIM_POST, 0, DIM_TRAVERSE_Y, DIM_TRAVERSE_Z, a_pos=pos(DIM_ALL_X-DIM_POST,DIM_POST,0), purch=purch_post_100_2_4)
traverse_angle_right.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_angle_right)

dim_front_width=pcad.Dimensioning(pcad.Point(DIM_POST/2,DIM_POST/2,0),pcad.Point(DIM_ALL_X-DIM_POST/2,DIM_POST/2,0),plane="-zx",prop=dim_prop)
l_objs.append(dim_front_width)

# middle
##############################################################################
# carrier_middle = pcad.sobj("carrier_middle", pos=pcad.pos(-DIM_POST, DIM_ALL_Y/2-DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_post)
# carrier_middle.add(pcad.cube(DIM_ALL_X + 2*DIM_POST, DIM_POST, DIM_POST))
# carrier_middle.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(DIM_POST, 0, 0)))
# carrier_middle.set_color(pcad.RGBColor.RED)
# l_objs.append(carrier_middle)

traverse_front_left = mac_cube_traverse_xz(DIM_POST,DIM_POST, DIM_TRAVERSE_X, DIM_TRAVERSE_Z, 0, a_pos=pos(DIM_POST, 0, 0), purch=purch_post_100_2_4)
traverse_front_left.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_front_left)

traverse_front_right = mac_cube_traverse_xz(DIM_POST,DIM_POST, 0,DIM_TRAVERSE_X, DIM_TRAVERSE_Z, a_pos=pos(DIM_ALL_X - DIM_POST- DIM_TRAVERSE_Z, 0, 0), purch=purch_post_100_2_4)
traverse_front_right.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_front_right)

traverse_middle_left = mac_cube_traverse_xz(DIM_POST,DIM_POST, DIM_TRAVERSE_X, DIM_TRAVERSE_Z, 0, a_pos=pos(DIM_POST,DIM_ALL_MID_Y-DIM_POST/2,0), purch=purch_post_100_2_4)
traverse_middle_left.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_middle_left)

traverse_middle_right = mac_cube_traverse_xz(DIM_POST,DIM_POST, 0,DIM_TRAVERSE_X, DIM_TRAVERSE_Z, a_pos=pos(DIM_ALL_X - DIM_POST- DIM_TRAVERSE_Z,DIM_ALL_MID_Y-DIM_POST/2,0), purch=purch_post_100_2_4)
traverse_middle_right.set_color(pcad.RGBColor.RED)
l_objs.append(traverse_middle_right)


# carrier_middle = pcad.sobj("carrier_middle", pos=pcad.pos(-DIM_POST, DIM_ALL_Y/2-DIM_POST, DIM_ALL_CARRIER_Z), purch=purch_post)
# carrier_middle.add(pcad.cube(DIM_ALL_X + 2*DIM_POST, DIM_POST, DIM_POST))
# carrier_middle.add(pcad.cube(DIM_POST, DIM_POST, DIM_POST/2, pos=pcad.pos(DIM_POST, 0, 0)))
# carrier_middle.set_color(pcad.RGBColor.RED)
# l_objs.append(carrier_middle)

pull_up_bar = tpl_barpullup.copy()
pull_up_bar.name = "pull_up_bar"
pull_up_bar.pos = pcad.pos(0, DIM_POST/2, DIM_PULL_UP_BAR_Z)
l_objs.append(pull_up_bar)

dip_bar_front = tpl_bardip.copy()
dip_bar_front.name = "dip_bar_front"
dip_bar_front.pos = pcad.pos(0, DIM_ALL_MID_Y, DIM_DIP_Z)
l_objs.append(dip_bar_front)

dip_bar_end = tpl_bardip.copy()
dip_bar_end.name = "dip_bar_end"
dip_bar_end.pos = pcad.pos(0, DIM_ALL_Y + DIM_POST/2, DIM_DIP_Z)
l_objs.append(dip_bar_end)

dim_traverse_heigh_1=pcad.Dimensioning(pcad.Point(0,post_left_end.pos.y,0),pcad.Point(0,post_left_end.pos.y,DIM_ALL_CARRIER_Z),plane="-yz",prop=dim_prop)
l_objs.append(dim_traverse_heigh_1)

# Execute
##############################################################################
prog_parse.exam_execute(l_objs)
pcad.purch_report(l_objs, f"{sys.argv[0]}.txt")