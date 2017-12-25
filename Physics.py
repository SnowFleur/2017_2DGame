from pico2d import *

import game_framework
from math import *


#충돌체크
def BoxCheck(a,b):
    left_a, bottom_a, right_a, top_a = a.ReturnBox()
    left_b, bottom_b, right_b, top_b = b.ReturnBox()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    print("충돌")
    return True
#시야 체크
def AiViewCheck(ai,unit):
    left_a,right_a,top_a,bottom_a = unit.ReturnCameraPosition()
    ai_xpos, ai_ypos=ai.ReturnPosition()
    if ai_xpos<left_a: return False
    if ai_xpos>right_a: return False
    if ai_ypos>top_a: return False
    if ai_ypos<bottom_a:return False

    print("시야에 들어옴")
    return True
def Win():
    pass

def Lose():
    pass


