from Unit_Class import *
from Map_Class import*
from Bullet_Class import *
from Title_state import *
from Font_Class import *
from AI_Class import *
from pico2d import *
from Physics import *
import game_framework


########################
# 전역변수
########################
g_aimframe=0  # 에임 프레임
g_button_type=[0,0] #마우스 버튼 타입 및 값
g_count=0   # 총알 갯수
g_rebound=0 #반동
g_rebound_time = 0  # 반동 시간 제한할 지역변수
g_temp_time=0
g_temp_image=None
def enter():
    global unit,map, g_mouse_aim   #유닛(클래스),맵(클래스),마우스에임(이미지)
    global shell,bullet  #탄피(클래스),총알(클래스)
    global font #폰트
    global ai,g_temp_image
#    balls = [Ball() for i in range(10)]
  #  open_canvas()  이어 줄떄애는 꺼야함
    unit = Unit()  # Unit 객체 생성
    map = Map()  # 맵 객체 생성
    ai=Ai() #ai 객체 색성
#    font=Font() # font 객체생성
    bullet=[Bullet() for i in range(100)] #총알 객체 생성
    shell=[Shell() for i in range(100)] # 탄피 객체 생성

    g_temp_image=load_image("resource/Main_Resource/win_box.png")
    g_mouse_aim=load_image("resource/UI/ReactionAim.png") #에임 이미지 로드

def exit():
    global unit,map,g_mouse_aim,bullet,shell,ai
    del (unit)
    del (map)
    del(g_mouse_aim)
    #배열이기 때문에 이렇게 지워도 될지 모르겠음 아니면 연결리스트 마냥 다 지워야 하는지
    del(bullet)
    del(shell)
    del(ai)
    close_canvas()


def draw(frame_time):
    global g_aimframe
    global  g_temp_time
    clear_canvas()
    map.Draw() #맵 생성

#    font.draw()

    ########################
    # 총알 및 탄피
    #########################
    for bullets in bullet:
        bullets.Draw()
    for shells in shell:
        shells.Darw()
    ########################
    # 유닛 및 무기
    #########################
    unit.Draw()
#    if g_temp_time<1200:
    ai.Draw()
#    else:
#        g_temp_image.draw(400,300)

    ########################
    # 마우스 커서 관련
    ########################
    g_mouse_aim.clip_draw(g_aimframe,0,50,50,g_mouse_x,g_mouse_y)
    g_temp_time+=1
    hide_cursor()
    update_canvas()


def handle_events(frame_time):
    MOUSE_DOWN,MOUSE_UP=True,False  #상수 매크로 정의
    #전역변수
    global g_mouse_x, g_mouse_y  #마우스 에임 좌표
    global g_button_type   #마우스 타입 및 값 저장 할 리스트(배열)
    global g_count   # 총알 카운터

    #지역변수
    position_y, position_x, position_rotate = 0, 0, 0  # 현재 유닛의 바라보는 방향과 위치 값 받을 지역변수
    #********************
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

            ########################
            # 총알 날리는 부분
            ########################
            position_rotate = unit.ReturnRotate()  # 유닛의 회전 좌표값
            position_x, position_y = unit.ReturnPositon()  # 유닛의 현재 좌표
            bullet[g_count].UnitPosition(position_x, position_y, position_rotate)
            bullet[g_count].Shot()  # 총알 날리
            ########################
            # 탄피 나오는 부분
            ########################
            shell[g_count].InputPosition(position_x,position_y)
            #+40,+20  나중에 오차 수정
            g_count+=1  #총알 카운터 증가


        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):  # 마우스클릭 (UP)
            g_button_type[0] = MOUSE_UP
            g_button_type[1] = 0
        else:
         unit.UnitControl(event)

    MouseClickEvents(g_button_type)



def MouseClickEvents(button):   #마우스를 누르고 있을때 처리할 함수
    MOUSE_DOWN, MOUSE_UP = True, False  # 상수 매크로 정의
    BUTTON_KIND, BUTTON_OPERATION = 0, 1  # 상수 매크로 정의
    REBOUND_MAXTIME = 2  #반동 최대 시간 (이걸 안주면 반동이 너무 심함)

    global g_aimframe,g_count  #클립이미지 옮길 변수
    global g_rebound,g_rebound_time #반동 값,반동 걸릴 시간
    #지역변수
    shot=False  #마우스 누르고 있을때 발사 시간 제한 할 스위치 지역변수
    position_y,position_x,position_rotate=0,0,0   # 현재 유닛의 바라보는 방향과 위치 값 받을 지역변수
    # ********************
    if(button[BUTTON_KIND]==MOUSE_DOWN):

        ########################
        # 총알 날리는 부분(연사 반동 부분)
        ########################
        position_rotate = unit.ReturnRotate()  # 유닛의 회전 좌표값 받기
        position_x, position_y = unit.ReturnPositon()  # 유닛의 현재 좌표 받기
        bullet[g_count].UnitPosition(position_x, position_y, position_rotate)  # 현재 유닛의 바라보는 방향과 위치 를 탄알 에게 줌

        shot=bullet[g_count].RateShot(g_rebound)  # 연속 총알 날리기
        if shot==True: #발싸 되면 트루 값 반환
            shell[g_count].InputPosition(position_x, position_y)  #탄피
            g_count += 1  # 총알 카운터 증가
            print("탄피값:%d",g_count)
            g_rebound_time+=1  #반동 시간 증가 (사실상 g_count 와 역할이 같음;;;)
            print("반동 시간 값 %d",g_rebound_time)
            if g_rebound_time>REBOUND_MAXTIME:
                if g_rebound<2:  #누르고 있는 동안은 반동값 증가
                    g_rebound+=0.5
                    g_rebound_time=0

        g_aimframe=min(240,g_aimframe+button[BUTTON_OPERATION])
        if g_aimframe>=240:
          g_aimframe-=120


    elif(button[BUTTON_KIND]==MOUSE_UP):
        if g_rebound>0:  #마우스를 때는 동안은 반동값 감소
            g_rebound-=0.5
            g_rebound_time-=1
            print("반동계수 %d,반동시간 %d",g_rebound,g_rebound_time)
        g_aimframe=min(0,g_aimframe-button[BUTTON_OPERATION])


def pause():
    pass


def resume():
    pass


def update(frame_time):
    Unit.UpDate(unit,frame_time)
    for bullets in bullet:
        bullets.Update(frame_time)
    for shells in shell:
        shells.Update(frame_time)

def get_frame_time():

    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time





