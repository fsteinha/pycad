import sys
sys.path.append("../")
import copy

import pcad.pcad as pcad
import obj.dimension.obj_dim as dim
import prog.prog_parse as prog_parse

# Table dimensions
##############################################################################

TABLE_HEIGH = 600
TABLE_INTER_HEIGH = 300 #must be 300 for the intermediate plate
TABLE_DEPTH = 850
TABLE_DEPTH_OFFSET = 1000
TABLE_WITH  = 2000
TABLE_SPACE_FROM_RIGTH = 600

# Enviroment objects
##############################################################################
HEATING_HEIGH = 1000
HEATING_WIDE  = 640
HEATING_DEPTH = 150
HEATING_POS_X = 740
HEATING_POS_y = 850


# Materials
##############################################################################

# Unterkonstruktionslatte https://www.bauhaus.info/latten-rahmen/unterkonstruktionslatte/p/20828565
Unterkonstruktionslatte_2000_40_18 = pcad.cube(40, 18, 2000)
# Rahmenholz https://www.bauhaus.info/latten-rahmen/rahmenholz/p/14612119
Rahmenholz_2000_54_54 = pcad.cube(54, 54, 2000)
# Speerholzplatte pine https://www.bauhaus.info/sperrholzplatten/sperrholzplatte-fixmass-elliotis-pine-cc/p/22300236
Sperrholzplatte = pcad.cube(2500,1250,12)


# Enviroment object definition
##############################################################################
heating = pcad.cube(HEATING_WIDE, HEATING_DEPTH,HEATING_HEIGH)
heating.pos = pcad.pos(HEATING_POS_X, HEATING_POS_y, 0)
heating.set_color(pcad.RGBColor.DARK_GREY)

# construction contrains
##############################################################################
# side pols (standing)
POLE_X = Rahmenholz_2000_54_54.dx
POLE_Y = Rahmenholz_2000_54_54.dy

#bar lying in x dimension
BARX_Y = Unterkonstruktionslatte_2000_40_18.dy
BARX_Z = Unterkonstruktionslatte_2000_40_18.dx

#bar lying in y dimension
BARY_X = Unterkonstruktionslatte_2000_40_18.dy
BARY_Z = Unterkonstruktionslatte_2000_40_18.dx

PLATE_INTER_Z = Sperrholzplatte.dz
# construction
##############################################################################

pole_left_front  = pcad.sobj()
pole_left_front.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_left_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGH-BARX_Z)))
pole_left_front.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGH-BARX_Z)))
pole_left_front.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))
pole_left_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_left_behind  = pcad.sobj(pos=pcad.pos(0,TABLE_DEPTH-POLE_Y,0))
pole_left_behind.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_left_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0, POLE_Y-BARX_Y,TABLE_HEIGH-BARX_Z)))
pole_left_behind.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0, 0, TABLE_HEIGH-BARX_Z)))
pole_left_behind.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0, 0, TABLE_INTER_HEIGH-BARX_Z)))
pole_left_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0, POLE_Y-BARX_Y, TABLE_INTER_HEIGH-BARX_Z)))

pole_right_front = pcad.sobj(pos=pcad.pos(TABLE_WITH-POLE_X,0,0))
pole_right_front.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_right_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGH-BARX_Z)))
pole_right_front.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(POLE_X-BARY_X, 0, TABLE_HEIGH-BARX_Z)))
pole_right_front.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(POLE_X-BARY_X, 0, TABLE_INTER_HEIGH-BARX_Z)))
pole_right_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_right_behind = pcad.sobj(pos=pcad.pos(TABLE_WITH-POLE_X,TABLE_DEPTH-POLE_Y,0))
pole_right_behind.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_right_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_HEIGH-BARX_Z)))
pole_right_behind.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(POLE_X-BARY_X, 0, TABLE_HEIGH-BARX_Z)))
pole_right_behind.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(POLE_X-BARY_X, 0, TABLE_INTER_HEIGH-BARX_Z)))
pole_right_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)))

pole_mid_front  = pcad.sobj(pos=pcad.pos(TABLE_WITH/2-POLE_X/2,0,0))
pole_mid_front.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_mid_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGH-BARX_Z)))
pole_mid_front.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_mid_behind  = pcad.sobj(pos=pcad.pos(TABLE_WITH/2-POLE_X/2,TABLE_DEPTH-POLE_Y,0))
pole_mid_behind.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGH))
pole_mid_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_HEIGH-BARX_Z)))
pole_mid_behind.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)))

cross_bar_front_top     = pcad.cube(TABLE_WITH, BARX_Y, BARX_Z)
cross_bar_front_top.set_color(pcad.RGBColor.DARK_RED)
cross_bar_front_top.pos = pcad.pos(0, 0, TABLE_HEIGH-BARX_Z)

cross_bar_behind_top = pcad.cube(TABLE_WITH-2*BARY_X, BARX_Y, BARX_Z)
cross_bar_behind_top.set_color(pcad.RGBColor.DARK_RED)
cross_bar_behind_top.pos = pcad.pos(BARY_X,TABLE_DEPTH-BARX_Y,TABLE_HEIGH-BARX_Z)

cross_bar_front_mid = copy.copy(cross_bar_front_top)
cross_bar_front_mid.pos = pcad.pos(BARY_X, 0, TABLE_INTER_HEIGH-BARX_Z)

cross_bar_behind_mid = copy.copy(cross_bar_behind_top)
cross_bar_behind_mid.pos = pcad.pos(BARY_X,TABLE_DEPTH-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)

cross_bar_left = pcad.cube(BARY_X, TABLE_DEPTH_OFFSET, BARX_Z)
cross_bar_left.pos = pcad.pos(0,0,TABLE_HEIGH-BARX_Z)
cross_bar_left.set_color(pcad.RGBColor.RED)

cross_bar_right = copy.copy(cross_bar_left)
cross_bar_right.pos = pcad.pos(TABLE_WITH-BARY_X, 0, TABLE_HEIGH-BARX_Z)

cross_bar_left_mid = pcad.cube(BARY_X, TABLE_DEPTH, BARX_Z)
cross_bar_left_mid.pos = pcad.pos(0, 0, TABLE_INTER_HEIGH-BARX_Z)
cross_bar_left_mid.set_color(pcad.RGBColor.RED)

cross_bar_right_mid = copy.copy(cross_bar_left_mid)
cross_bar_right_mid.pos = pcad.pos(TABLE_WITH-BARY_X, 0, TABLE_INTER_HEIGH-BARX_Z)

cross_bar_l1 = copy.copy(cross_bar_left)
cross_bar_l1.pos = pcad.pos(HEATING_POS_X - 2*BARY_X, 0, TABLE_HEIGH-BARX_Z)

cross_bar_l2 = copy.copy(cross_bar_left)
cross_bar_l2.pos = pcad.pos(TABLE_WITH - TABLE_SPACE_FROM_RIGTH, 0, TABLE_HEIGH-BARX_Z)

cross_bar_c1 = pcad.cube(TABLE_WITH- TABLE_SPACE_FROM_RIGTH + BARY_X, BARX_Y, BARX_Z, pos=pcad.pos(0, TABLE_DEPTH/2, TABLE_HEIGH-BARX_Z))
cross_bar_c1.set_color(pcad.RGBColor.DARK_RED)

plate_inter = pcad.sobj(pos=pcad.pos(0,0,TABLE_INTER_HEIGH))
plate_inter.add(pcad.cube(TABLE_WITH, TABLE_DEPTH, PLATE_INTER_Z))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z, pos=pcad.pos(TABLE_WITH-POLE_X,0                 ,0)))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z, pos=pcad.pos(0                ,TABLE_DEPTH-POLE_Y,0)))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z, pos=pcad.pos(TABLE_WITH-POLE_X,TABLE_DEPTH-POLE_Y,0)))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z, pos=pcad.pos((TABLE_WITH-POLE_X)/2,0,0)))
plate_inter.add(pcad.cube(POLE_X    , POLE_Y     , PLATE_INTER_Z, pos=pcad.pos((TABLE_WITH-POLE_X)/2,TABLE_DEPTH-POLE_Y,0)))
plate_inter.set_color(pcad.RGBColor.DARK_GREY)

# object_list
##############################################################################

obj_list = [
    heating,
    pole_left_behind,
    pole_left_front,
    pole_right_behind,
    pole_right_front,
    pole_mid_front,
    pole_mid_behind,
    cross_bar_front_top,
    cross_bar_behind_top,
    cross_bar_front_mid,
    cross_bar_behind_mid,
    cross_bar_left,
    cross_bar_right,
    cross_bar_left_mid,
    cross_bar_right_mid,
    cross_bar_l1,
    cross_bar_l2,
    cross_bar_c1,
    plate_inter
]


# show
##############################################################################
prog_parse.exam_execute(obj_list)

