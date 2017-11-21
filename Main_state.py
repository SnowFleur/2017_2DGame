from pico2d import *
from Unit_Class import *
from Map_Class import*
from Bullet_Class import *
from Title_state import *
import game_framework

########################
# 전역변수
########################
g_aimframe=0  # 에임 프레임
g_button_type=[0,0] #마우스 버튼 타입 및 값
g_shell=None  #탄피
g_count=0
temp=0   #임시 돌리기 변수
def enter():
    global unit,map, g_mouse_aim   #유닛(클래스),맵(클래스),마우스에임(이미지)
    global g_shell,bullet
#    balls = [Ball() for i in range(10)]
    open_canvas()
    unit = Unit()  # Unit 객체 생성
    map = Map()  # 맵 객체 생성
    bullet=[Bullet() for i in range(100)] #총알 객체 생성
    g_mouse_aim=load_image("resource/UI/ReactionAim.png") #에임 이미지 로드
    g_shell=load_image("resource/UI/shell.png") #탄피 이미지 로드



def exit():
    global unit,map,g_mouse_aim,bullet
    del (unit)
    del (map)
    del(g_mouse_aim)
    del(bullet)
    close_canvas()


def draw(frame_time):
    global g_aimframe
    global g_shell
    global temp
    clear_canvas()
  #  map.Draw() #맵 생성


    unit.Draw()
    for bullets in bullet:
        bullets.Draw()

    g_shell.rotate_draw(temp,400,300,50,100)

    draw_rectangle(0,0,100,100)

    if temp<6.5:
        temp+=0.005


    ########################
    # 마우스 커서 관련
    ########################
    g_mouse_aim.clip_draw(g_aimframe,0,50,50,g_mouse_x,g_mouse_y)
    hide_cursor()
    update_canvas()

def handle_events(frame_time):
    global g_mouse_x, g_mouse_y  #마우스 에임 좌표
    global g_button_type   #마우스 타입 및 값 저장 할 리스트(배열)
    global g_count
    MOUSE_DOWN,MOUSE_UP=True,False  #상수 매크로 정의
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:  # 마우스 on
            x, y = event.x, 600 - event.y
            g_mouse_x, g_mouse_y = x, y  # 마우스 이미지 변수
        elif (event.type,event.button) == (SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT): #마우스클릭 (DWON)
            g_button_type[0]=MOUSE_DOWN
            g_button_type[1]=60
            bullet[g_count].Shot()   #총알 날리기
            positon_x, position_y = unit.ReturnPositon()
            bullet[g_count].UnitPosition(positon_x + 40, position_y + 20)
            g_count+=1

            print("%d,%d",positon_x,position_y)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):  # 마우스클릭 (UP)
            g_button_type[0] = MOUSE_UP
            g_button_type[1] = 0
        else:
         unit.UnitControl(event)

    MouseClickEvents(g_button_type)



def MouseClickEvents(button):
    global g_aimframe  #클립이미지 옮길 변수
    MOUSE_DOWN,MOUSE_UP=True,False  # 상수 매크로 정의
    BUTTON_KIND,BUTTON_OPERATION=0,1# 상수 매크로 정의

    if(button[BUTTON_KIND]==MOUSE_DOWN):
        g_aimframe=min(240,g_aimframe+button[BUTTON_OPERATION])
        if g_aimframe>=240:
          g_aimframe-=120
    elif(button[BUTTON_KIND]==MOUSE_UP):
        g_aimframe=min(0,g_aimframe-button[BUTTON_OPERATION])

def pause():
    pass


def resume():
    pass


def update(frame_time):
    Unit.UpDate(unit,frame_time)
    for bullets in bullet:
        bullets.Update(frame_time)



def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time





