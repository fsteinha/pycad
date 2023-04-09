import sys
sys.path.append("../src")
import copy

import pcad as pcad
import const_scad
import dimensioning as dim
import const_cadquery
import exam_parse

# Table dimensions
##############################################################################

TABLE_HEIGTH = 600
TABLE_INTER_HEIGH = 100
TABLE_DEPTH = 850
TABLE_DEPTH_OFFSET = 1000
TABLE_WITH  = 2000
TABLE_SPACE_FROM_RIGTH = 600

# Materials
##############################################################################

# Unterkonstruktionslatte https://www.bauhaus.info/latten-rahmen/unterkonstruktionslatte/p/20828565
Unterkonstruktionslatte_2000_40_18 = pcad.cube(40, 18, 2000)
# Rahmenholz https://www.bauhaus.info/latten-rahmen/rahmenholz/p/14612119
Rahmenholz_2000_54_54 = pcad.cube(54, 54, 2000)

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

# construction types
##############################################################################

pole_t1 = pcad.sobj("pole_t1")
pole_t1.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGTH))
pole_t1.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t1.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t1.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))
pole_t1.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_t2 = pcad.sobj("pole_t2")
pole_t2.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGTH))
pole_t2.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t2.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t2.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))
pole_t2.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_t3 = pcad.sobj("pole_t3")
pole_t3.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGTH))
pole_t3.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_HEIGTH-BARX_Z)))
pole_t3.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t3.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)))
pole_t3.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_t4 = pcad.sobj("pole_t4")
pole_t4.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGTH))
pole_t4.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t4.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t4.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))
pole_t4.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

pole_t5 = pcad.sobj("pole_t5")
pole_t5.add(pcad.cube(POLE_X, POLE_Y, TABLE_HEIGTH))
pole_t5.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_HEIGTH-BARX_Z)))
pole_t5.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)))
pole_t5.add(pcad.cube(POLE_X, BARX_Y, BARX_Z, pos=pcad.pos(0,POLE_Y-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)))
pole_t5.add(pcad.cube(BARY_X, POLE_Y, BARX_Z, pos=pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)))

crossbar_x_front = pcad.cube(TABLE_WITH,
                       Unterkonstruktionslatte_2000_40_18.dy,
                       Unterkonstruktionslatte_2000_40_18.dx)
crossbar_x_front.set_color(pcad.RGBColor.DARK_RED)

crossbar_x_behind = pcad.cube(TABLE_WITH - 2 * Unterkonstruktionslatte_2000_40_18.dy,
                       Unterkonstruktionslatte_2000_40_18.dy,
                       Unterkonstruktionslatte_2000_40_18.dx)
crossbar_x_behind.set_color(pcad.RGBColor.DARK_RED)


crossbar_y = pcad.cube(Unterkonstruktionslatte_2000_40_18.dy,
                       TABLE_DEPTH - 2 *Unterkonstruktionslatte_2000_40_18.dy,
                       Unterkonstruktionslatte_2000_40_18.dx)
crossbar_y.set_color(pcad.RGBColor.RED)

crossbar_y_top = pcad.cube(Unterkonstruktionslatte_2000_40_18.dy,
                       TABLE_DEPTH_OFFSET - Unterkonstruktionslatte_2000_40_18.dy,
                       Unterkonstruktionslatte_2000_40_18.dx)
crossbar_y_top.set_color(pcad.RGBColor.RED)

# construction
##############################################################################

pole_left_behind = copy.copy(pole_t1)
pole_left_behind.pos = pcad.pos(0,TABLE_DEPTH,0)
pole_left_behind.rot = pcad.rot(0,0,-90)
pole_left_behind.set_name(None)

pole_left_front  = copy.copy(pole_t1)
pole_left_front.set_name(None)

pole_right_behind = copy.copy(pole_t3)
pole_right_behind.pos = pcad.pos(TABLE_WITH-POLE_X,TABLE_DEPTH,0)
pole_right_behind.rot = pcad.rot(0,0,-90)
pole_right_behind.set_name(None)

pole_right_front  = copy.copy(pole_t2)
pole_right_front.pos = pcad.pos(TABLE_WITH,0,0)
pole_right_front.rot = pcad.rot(0,0,90)
pole_right_front.set_name(None)

pole_middle_front  = copy.copy(pole_t4)
pole_middle_front.pos = pcad.pos(TABLE_WITH-TABLE_SPACE_FROM_RIGTH,0,0)
pole_middle_front.rot = pcad.rot(0,0,90)
pole_middle_front.set_name(None)

pole_middle_behind  = copy.copy(pole_t5)
pole_middle_behind.pos = pcad.pos(TABLE_WITH-TABLE_SPACE_FROM_RIGTH-POLE_X,TABLE_DEPTH,0)
pole_middle_behind.rot = pcad.rot(0,0,-90)
pole_middle_behind.set_name(None)

cross_bar_front_top = copy.copy(crossbar_x_front)
cross_bar_front_top.pos = pcad.pos(0,0,TABLE_HEIGTH-BARX_Z)
cross_bar_front_top.set_name(None)

cross_bar_behind_top = copy.copy(crossbar_x_behind)
cross_bar_behind_top.pos = pcad.pos(Unterkonstruktionslatte_2000_40_18.dy,TABLE_DEPTH-BARX_Y,TABLE_HEIGTH-BARX_Z)
cross_bar_behind_top.set_name(None)

cross_bar_front_mid = copy.copy(crossbar_x_front)
cross_bar_front_mid.pos = pcad.pos(0,0,TABLE_INTER_HEIGH-BARX_Z)
cross_bar_front_mid.set_name(None)

cross_bar_behind_mid = copy.copy(crossbar_x_front)
cross_bar_behind_mid.pos = pcad.pos(0,TABLE_DEPTH-BARX_Y,TABLE_INTER_HEIGH-BARX_Z)
cross_bar_behind_mid.set_name(None)

cross_bar_left = copy.copy(crossbar_y_top)
cross_bar_left.pos = pcad.pos(0,cross_bar_left.dx,TABLE_HEIGTH-BARX_Z)
cross_bar_left.set_name(None)

cross_bar_right = copy.copy(crossbar_y_top)
cross_bar_right.pos = pcad.pos(TABLE_WITH-cross_bar_right.dx,cross_bar_right.dx,TABLE_HEIGTH-BARX_Z)
cross_bar_right.set_name(None)

cross_bar_left_mid = copy.copy(crossbar_y)
cross_bar_left_mid.pos = pcad.pos(0,cross_bar_left_mid.dx,TABLE_INTER_HEIGH-BARX_Z)
cross_bar_left_mid.set_name(None)

cross_bar_right_mid = copy.copy(crossbar_y)
cross_bar_right_mid.pos = pcad.pos(TABLE_WITH-cross_bar_right_mid.dx,cross_bar_right_mid.dx,TABLE_INTER_HEIGH-BARX_Z)
cross_bar_right_mid.set_name(None)

# show
##############################################################################

if exam_parse.M_SCAD==True:
    scad = const_scad.scad_const(exam_parse.get_const_name(__file__),
                                 pole_left_behind,
                                 pole_left_front,
                                 pole_right_behind,
                                 pole_right_front,
                                 pole_middle_front,
                                 pole_middle_behind,
                                 cross_bar_front_top,
                                 cross_bar_behind_top,
                                 cross_bar_front_mid,
                                 cross_bar_behind_mid,
                                 cross_bar_left,
                                 cross_bar_right,
                                 cross_bar_left_mid,
                                 cross_bar_right_mid)
    scad.show()
else:
    constcq = const_cadquery.cq_const(exam_parse.get_const_name(__file__), pole_t1)
    constcq.show()
