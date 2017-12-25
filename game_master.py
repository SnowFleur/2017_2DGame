import game_framework
from pico2d import *
import Main_state
import Title_state
# 640,360
#open_canvas()   #메인타이틀 은 이걸 주석 안하면 안꺼짐 추후 수정할것
game_framework.run(Main_state)
close_canvas()