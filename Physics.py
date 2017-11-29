from pico2d import *

import game_framework






def BoxCheck(a,b):
    left_a, bottom_a, right_a, top_a = a.ReturnBox()
    left_b, bottom_b, right_b, top_b = b.ReturnBox()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    print("충돌")
    return True



def Win():
    pass

def Lose():
    pass


