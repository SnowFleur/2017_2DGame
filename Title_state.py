
import game_framework
from pico2d import *



selectgun_image=None #총 선택 틀
Button_animatino=None # 버튼 애니메이션
Button_play_off=None  #마우스 올리기 전
Button_play_on=None   # 마우스 올린 후
def enter():
    global selectgun_image,Button_animatino,Button_play_on,Button_play_off
    selectgun_image=load_image('resource/Title_Resource/SelectGun.png')
    Button_animatino=load_image('resource/Title_Resource/Button_ani.png')
    Button_play_off=load_image('resource/Title_Resource/Button_play_off.png')
    Button_play_on=load_image('resource/TItle_Resource/Button_play_on.png')
def exit():
    global selectgun_image,Button_animatino,Button_play_on,Button_play_off
    del(selectgun_image)
    del(Button_play_off)
    del(Button_animatino)
    del(Button_play_on)
    close_canvas()
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    global selectgun_image,Button_animatino,Button_play_on,Button_play_off

    clear_canvas()
    selectgun_image.draw(485,180
    Button_play_off.draw(485,180)
    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass






