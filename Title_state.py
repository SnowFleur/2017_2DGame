
import game_framework
from pico2d import *


frame,timer=0,0
g_posresult=None
g_wapenpos=0
#열거형
g_arrow_table=["MAIN_LEFT","MAIN_RIGHT","SUB_LEFT","SUB_RIGHT","SUB2_LEFT","SUB2_RIGHT","PLAY_GAME"]

#추후 줄일 수 있는 배열 혹은 여러가지 방법 생각해보기
#추후 코드 정리
g_select_imag=None #총 선택 틀
g_btn_animag=None # 버튼 애니메이션
g_btnoff_imag=None  #마우스 올리기 전
g_btnon_imag=None   # 마우스 올린 후
g_select_arrow_imag=None  #선택 화살표
g_mwapen_imag=None # 메인 웨폰 이미지
g_swapen_imag=None #사이드 웨폰 이미지
g_grenades_imag=None # 수류탄 이미지
g_line_animg=None #라인 애니메이션

def enter():
    global g_select_imag, g_btn_animag,g_btnon_imag,g_btnoff_imag,g_select_arrow_imag,g_mwapen_imag,g_swapen_imag,g_grenades_imag,g_line_animg
    g_select_imag=load_image('resource/Title_Resource/SelectGun2.png')    #선택 창
    g_btn_animag=load_image('resource/Title_Resource/Button_ani.png')  # 버튼 애니매이션
    g_btnoff_imag=load_image('resource/Title_Resource/Button_play_off.png') #플레이 버튼  off
    g_btnon_imag=load_image('resource/TItle_Resource/Button_play_on.png')   # 플레이 버튼 on
    g_select_arrow_imag=load_image('resource/Title_Resource/LEFT_RIGHT.png')  #화살표 애니메이션
    g_mwapen_imag=load_image('resource/Title_Resource/Wapen_Scroll.png')     # 무기스크롤
def exit():
    global g_select_imag, g_btn_animag, g_btnon_imag, g_btnoff_imag, g_select_arrow_imag, g_mwapen_imag, g_swapen_imag, g_grenades_imag, g_line_animg
    del(g_select_imag)
    del(g_btn_animag)
    del(g_btnon_imag)
    del(g_btnoff_imag)
    del(g_select_arrow_imag)
    del(g_mwapen_imag)
    del(g_swapen_imag)
#    del (g_grenades_imag)
#    del (g_line_animg)
    close_canvas()



#추후 정리 선 작동유무 ,후 정리
#전역변수 선언됨 프레임 및 타이머 또한 함수 처리
def draw():
    global g_select_imag, g_btn_animag, g_btnon_imag, g_btnoff_imag, g_select_arrow_imag, g_mwapen_imag, g_swapen_imag, g_grenades_imag, g_line_animg
    global frame,timer
    global g_test_mouse
    clear_canvas()
    g_select_imag.draw(485,180)
    # 1. 가로 , 2. 세로,가로넓이,세로넓이,
  #  self.image.clip_draw(self.frame_ * 70, 200, 50, 50, 100, 100)

    #가로,세로 가로넓이,세로넓이  좌표,가로세로 크기
    g_btn_animag.clip_draw(frame*105, 0, 110, 100,635,30,50,50)
    if timer<=100:
        frame=1
        timer+=1
    elif 100<=timer and timer<230:
        timer+=1
        frame=0
    else:
        timer=0

    g_mwapen_imag.clip_draw(g_wapenpos,0,150,100,475,275)

    if(g_posresult=="MAIN_LEFT"):
        g_select_arrow_imag.clip_draw(25, 0, 25, 25, 397, 232)  # 왼쪽
    else:
        g_select_arrow_imag.clip_draw(0, 0, 25, 25, 397, 232)  # 왼쪽

    if (g_posresult == "MAIN_RIGHT"):
            g_select_arrow_imag.clip_draw(75, 0, 25, 25, 550, 232)  # 오른쪽
    else:
     g_select_arrow_imag.clip_draw(50, 0, 25, 25, 550, 232)  # 오른쪽
    if(g_posresult=="PLAY_GAME"):
        g_btnoff_imag.draw(725,30,120,60) #마우스 off
    else:
        g_btnon_imag.draw(725,30,120,60) #마우스 on

   # draw_rectangle(670,5,780,50)


    update_canvas()



def update():
    pass


def pause():
    pass


def resume():
    pass



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type==SDL_MOUSEMOTION:  # 마우스 on
            x, y = event.x, 600 - event.y
            MouseMotion(x,y)  # 마우스 모션 함수
        if event.type==SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 600 - event.y
            MouseClick(x, y)  # 마우스 모션 함수



def MouseClick(x,y):
    global g_wapenpos
    if (x >= 386 and x <= 406) and (y >= 223 and y <= 241):  # 왼쪽 화살표
        g_wapenpos=max(0,g_wapenpos-150)
    elif (x >= 539 and x <= 559) and (y >= 223 and y <= 241):  # 오른쪽 화살표
        g_wapenpos=min(900,g_wapenpos+150)


def MouseMotion(x,y):
    global g_posresult
    if (x>=386 and x<= 406) and (y >=223 and y <= 241): #왼쪽 화살표
        g_posresult=g_arrow_table[0]
    elif (x >= 539 and x <= 559) and (y >= 223 and y <= 241): # 오른쪽 화살표
        g_posresult=g_arrow_table[1]
    elif (x >= 670 and x <= 780) and (y >= 5 and y <= 50):  # 플레이 버튼
        g_posresult=g_arrow_table[6]
    else:
        g_posresult=None