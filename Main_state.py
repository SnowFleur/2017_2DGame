from pico2d import *
from Class import *
import game_framework



def enter():
    global unit,map
    open_canvas()
    unit = Unit()  # Unit 객체 생성
    map = Map()  # 맵 객체 생성

def exit():
    global unit,map
    del (unit)
    del (map)
    close_canvas()

def update():
    pass
def draw():
    clear_canvas()
    map.Draw() #맵 생성
#    unit.UnitControl()

    unit.Draw()

    delay(0.085)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
         unit.UnitControl(event)

def pause():
    pass


def resume():
    pass






