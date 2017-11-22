from pico2d import *

import game_framework






def BoxCheck( first,second):
    left_a, bottom_a, right_a, top_a =first.ReturnBox
    left_b, bottom_b, right_b, top_b = second.ReturnBox


    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def Win():
    pass

def Lose():
    pass


