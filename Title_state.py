
#추후 줄일 수 있는 배열 혹은 여러가지 방법 생각해보기
#추후 코드 정리

import game_framework
from pico2d import *

########################
# 전역변수
########################
g_main_scroll,g_sub_scroll,g_sub2_scroll=0,0,0  # 이동 스크롤 값
g_button_value=[0, 0]  # 버튼 애니메이션을 처리해줄 변수
g_posresult=0
g_mouse_x,g_mouse_y=0,0
########################
# 상수 변수
########################
#상수 정의 나중에 튜플이나 딕셔너리로 변경 요망
g_arrow_table=["MAIN_LEFT","MAIN_RIGHT","SUB_LEFT","SUB_RIGHT","SUB2_LEFT","SUB2_RIGHT","PLAY_GAME"]

########################
# 이미지 관련 변수
########################
g_select_imag=None #총 선택 틀
g_btn_animag=None # 버튼 애니메이션
g_btnoff_imag=None  #마우스 올리기 전
g_btnon_imag=None   # 마우스 올린 후
g_mouse_imag=None  #마우스 이미지
g_select_arrow_imag=None  #선택 화살표
g_mweapon_imag=None # 메인 웨폰 이미지
g_sweapon_imag=None #사이드 웨폰 이미지
g_grenades_imag=None # 수류탄 이미지
g_line_animg=None #라인 애니메이션
g_background_imag=None #배경이미지
def enter():
    global g_select_imag, g_btn_animag,g_btnon_imag,g_btnoff_imag,g_select_arrow_imag,g_mweapon_imag,g_sweapon_imag,g_grenades_imag,g_line_animg, g_mouse_imag,g_background_imag
    g_select_imag=load_image('resource/Title_Resource/SelectGun3.png')    #선택 창
    g_btn_animag=load_image('resource/Title_Resource/Button_ani.png')  # 버튼 애니매이션
    g_btnoff_imag=load_image('resource/Title_Resource/Button_play_off.png') #플레이 버튼  off
    g_btnon_imag=load_image('resource/TItle_Resource/Button_play_on.png')   # 플레이 버튼 on
    g_select_arrow_imag=load_image('resource/Title_Resource/LEFT_RIGHT.png')  #화살표 애니메이션
    g_mweapon_imag=load_image('resource/Title_Resource/Wapen_Scroll.png')     # 무기스크롤
    g_sweapon_imag=load_image('resource/Title_Resource/HG_Scroll.png')     # 보조무기스크롤
    g_mouse_imag = load_image('resource/Title_Resource/ArrowCursor.png')  # 마우스 이미지
    g_background_imag = load_image('resource/Title_Resource/BG.png')  # 배경화면
    g_grenades_imag=load_image('resource/Title_Resource/grenades_Scroll.png')   # 수류탄 스크롤
#    g_line_animg=load_image('resource/Title_Resource/HG_Scrool.png')    #라인 애니메이션

def exit():
    global g_select_imag, g_btn_animag, g_btnon_imag, g_btnoff_imag, g_select_arrow_imag, g_mweapon_imag, g_sweapon_imag, g_grenades_imag, g_line_animg, g_mouse_imag, g_background_ima
    del(g_select_imag)
    del(g_btn_animag)
    del(g_btnon_imag)
    del(g_btnoff_imag)
    del(g_select_arrow_imag)
    del(g_mweapon_imag)
    del(g_sweapon_imag)
    del (g_grenades_imag)
    del (g_line_animg)
    del(g_mouse_imag)
    del(g_background_imag)
    close_canvas()


#추후 정리 선 작동유무 ,후 정리
#전역변수 선언됨 프레임 및 타이머 또한 함수 처리
def draw(frame_time):
    global g_select_imag, g_btn_animag, g_btnon_imag, g_btnoff_imag, g_select_arrow_imag, g_mweapon_imag, g_sweapon_imag, g_grenades_imag, g_line_animg, g_mouse_imag, g_backgro#이미지
    global g_button_value,g_mouse_x,g_mouse_y
    clear_canvas()
    #g_background_imag.draw(400,300,800,600)

    g_select_imag.draw(485,180)
    ########################
    # 버튼 이미지 관련
    ########################
    ButtonAnimation(g_button_value)
    g_btn_animag.clip_draw(g_button_value[1]*105, 0, 110, 100,635,30,50,50)
    ########################
    # 메인무기 이미지 관련
    ########################
    g_mweapon_imag.clip_draw(g_main_scroll,0,150,100,475,275)  #메인무기 스크롤
    if(g_posresult=="MAIN_LEFT"):
        g_select_arrow_imag.clip_draw(25, 0, 25, 25, 397, 232)  # 왼쪽
    else:
        g_select_arrow_imag.clip_draw(0, 0, 25, 25, 397, 232)  # 왼쪽
    if (g_posresult == "MAIN_RIGHT"):
            g_select_arrow_imag.clip_draw(75, 0, 25, 25, 550, 232)  # 오른쪽
    else:
     g_select_arrow_imag.clip_draw(50, 0, 25, 25, 550, 232)  # 오른쪽
    ########################
    #  보조무기 이미지 관련
    ########################
    g_sweapon_imag.clip_draw(g_sub_scroll,0,150,80,360,100)  #보조무기 스크롤
    if(g_posresult=="SUB_LEFT"):
        g_select_arrow_imag.clip_draw(25, 0, 25, 25, 321, 70)  # 왼쪽
    else:
        g_select_arrow_imag.clip_draw(0, 0, 25, 25, 321, 70)  # 왼쪽
    if (g_posresult == "SUB_RIGHT"):
        g_select_arrow_imag.clip_draw(75, 0, 25, 25, 407, 70)  # 오른쪽
    else:
        g_select_arrow_imag.clip_draw(50, 0, 25, 25, 407, 70)  # 오른쪽
    ########################
    #  수류탄 이미지 관련
    ########################
    g_grenades_imag.clip_draw(g_sub2_scroll, 0, 150, 100, 517, 107)  # 보조무기 스크롤
    if (g_posresult == "SUB2_LEFT"):
        g_select_arrow_imag.clip_draw(25, 0, 25, 25, 478, 70)  # 왼쪽
    else:
        g_select_arrow_imag.clip_draw(0, 0, 25, 25, 478, 70)  # 왼쪽
    if (g_posresult == "SUB2_RIGHT"):
        g_select_arrow_imag.clip_draw(75, 0, 25, 25, 564, 70)  # 오른쪽
    else:
        g_select_arrow_imag.clip_draw(50, 0, 25, 25, 564, 70)  # 오른쪽




    ########################
    # 스타트 이미지 관련
    ########################
    if(g_posresult=="PLAY_GAME"):
        g_btnoff_imag.draw(725,30,120,60) #마우스 off
    else:
        g_btnon_imag.draw(725,30,120,60) #마우스 on



    ########################
    # 마우스 커서 관련
    ########################
    g_mouse_imag.draw(g_mouse_x + 13, g_mouse_y - 16, 120, 120)
    hide_cursor()
    update_canvas()

def handle_events(frame_time):
    global g_mouse_x,g_mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type==SDL_MOUSEMOTION:  # 마우스 on
            x, y = event.x, 600 - event.y
            g_mouse_x,g_mouse_y=x,y     #마우스 이미지 변수
            MouseMotion(x,y)  # 마우스 모션 함수
        if event.type==SDL_MOUSEBUTTONDOWN: #마우스 클릭
            x, y = event.x, 600 - event.y
            MouseClick(x, y)  # 마우스 모션 함수



def MouseClick(x,y):   #마우스 클릭 처리 함수
    global g_main_scroll,g_sub_scroll
    if (x >= 386 and x <= 406) and (y >= 223 and y <= 241):  # 메인무기 왼쪽 화살표
        g_main_scroll=max(0,g_main_scroll-150)
    elif (x >= 539 and x <= 559) and (y >= 223 and y <= 241):  # 메인무기 오른쪽 화살표
        g_main_scroll=min(900,g_main_scroll+150)
    elif (x >= 311 and x <= 330) and (y >= 60 and y <= 80):  # 보조무기 왼쪽 화살표
        g_sub_scroll=max(0,g_sub_scroll-150)
    elif (x >= 396 and x <= 417) and (y >= 60 and y <= 80):  # 보조무기 오른쪽 화살표
        g_sub_scroll = min(300, g_sub_scroll +150)

def MouseMotion(x,y): # 마우스 모션 처리 함수
    global g_posresult
    if (x>=386 and x<= 406) and (y >=223 and y <= 241): # 메인무기 왼쪽 화살표
        g_posresult=g_arrow_table[0]
    elif (x >= 539 and x <= 559) and (y >= 223 and y <= 241): # 메인무기 오른쪽 화살표
        g_posresult=g_arrow_table[1]
    elif (x >= 311 and x <= 330) and (y >= 60 and y <= 80): # 보조무기 왼쪽 화살표
        g_posresult=g_arrow_table[2]
    elif (x >= 396 and x <= 417) and (y >= 60 and y <= 80): # 보조무기 오른쪽 화살표
        g_posresult=g_arrow_table[3]
    elif (x >= 466 and x <= 490) and (y >= 60 and y <= 80):  # 수류탄 왼쪽 화살표
        g_posresult = g_arrow_table[4]
    elif (x >= 552 and x <= 576) and (y >= 60 and y <= 80):  # 수류탄 오른쪽 화살표
        g_posresult = g_arrow_table[5]
    elif (x >= 670 and x <= 780) and (y >= 5 and y <= 50):  # 플레이 버튼
        g_posresult=g_arrow_table[6]
    else:
        g_posresult=None

def ButtonAnimation(button_value): # 간단한 버튼 애니메이션

    if button_value[0] <= 100:    #타이머
        button_value[1] = 1      # 프레임
        button_value[0] += 1     # 프레임
    elif 100 <= button_value[0] and button_value[0] < 230:   #타이머
        button_value[0] += 1  # 타이머
        button_value[1] = 0   #프레임
    else:
        button_value[0] = 0  #타이머
    #    if timer <= 100:
    #        frame = 1
    #        timer += 1
    #    elif 100 <= timer and timer < 230:
    #        timer += 1
    #        frame = 0
    #    else:
    #        timer = 0


def update(frame_time):
    pass
def pause():
    pass
def resume():
    pass

