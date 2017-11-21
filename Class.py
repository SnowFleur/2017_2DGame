from pico2d import *
from Title_state import *
import Main_state
from math import *
import Main_state


class Map:
    #상수 매크로 정의
    FIRST_MAP,SECOND_MAP=1,2
    def __init__(self):  #생성과 동시에 두개의 맵 이미지 로드
        self.selectmap_=self.SECOND_MAP # 임시로 첫번쨰 맵만 로딩
        self.firstmap_=load_image('resource/map/map1.png')
        self.secondmap_ = load_image('resource/map/map2.png')
    def Draw(self):  #상수 매크로 에 따른 맵 그리기
        if(self.selectmap_==self.FIRST_MAP):
            self.firstmap_.draw(400,300)
        elif(self.selectmap_==self.SECOND_MAP):
            self.secondmap_.draw(400,300)

class Unit:

    PIXEL_PER_METER=(10.0/0.3)  #10 pixel 30cm
    RUN_SPPED_KMPH=20.0   #시간당 20km
    RUN_SPEED_MPH=(RUN_SPPED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPH/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS* PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    #상수 매크로 정의
    USAS,AWP,SCAR,M4,M16A1,MP5,UMP=0,150,300,450,600,750,900
    ANACONDA,D_EAGLE,GLOCK=0,150,300
    main_gun,hand_gun=None,None
    KEY_DOWN,KEY_UP=True,False
    LEFT_KEY,RIGHT_KEY,UP_KEY,DOWN_KEY=0,1,2,3
    def __init__(self):
        self.xmove_,self.ymove_=0,0    #키보드 연속 입력처리를 위한 변수
        self.xpos_,self.ypos_=100,100 # 실질적인 객체 위치 값
        self.rotate_=0 # 마우스 위치에 따른 객체 회전
        self.keyindex=[False,False,False,False] #키보드 인덱스
        if(Unit.main_gun==None):
            self.LoadImage()

    def Draw(self):    #Left,Bottom,가로길이,세로길이,x,y,
        Unit.main_gun.rotate_draw(self.rotate_,self.xpos_,self.ypos_)

    def UpDate(self, frame_time):
        print(" 마우스 %d",Main_state.g_mouse_y)
        self.rotate_=atan2( -(Main_state.g_mouse_x-self.xpos_) ,( Main_state.g_mouse_y-self.ypos_ ))

        distance = Unit.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.ymove_*distance)
        self.xpos_ += (self.xmove_*distance)


    def UnitControl(self, event):
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT): #왼쪽 이동
            self.xmove_=-1
            print("왼쪽")
            self.keyindex[self.LEFT_KEY]=self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):  # 오른쪽 이동
            self.xmove_= 1
            print("오른쪽")
            self.keyindex[self.RIGHT_KEY] = self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):  # 위쪽 이동
                self.ymove_ = 1
                print("위쪽")
                self.keyindex[self.UP_KEY] = self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):  # 아래쪽 이동
                self.ymove_ = -1
                print("아래쪽")
                self.keyindex[self.DOWN_KEY] = self.KEY_DOWN
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):  # 왼쪽 업
            if self.keyindex[self.RIGHT_KEY]==self.KEY_DOWN:
                self.xmove_ = 1
                self.keyindex[self.LEFT_KEY]=self.KEY_UP
            else:
                self.xmove_=0
                self.keyindex[self.LEFT_KEY]=self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):  # 오른쪽 업
            if self.keyindex[self.LEFT_KEY] == self.KEY_DOWN:
                self.xmove_ = -1
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP
            else:
                self.xmove_=0
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):  # 윗키 업
            if self.keyindex[self.DOWN_KEY]==self.KEY_DOWN:
                self.ymove_ = -1
                self.keyindex[self.UP_KEY]=self.KEY_UP
            else:
                self.ymove_=0
                self.keyindex[self.UP_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):  # 아래키 업
            if self.keyindex[self.UP_KEY] == self.KEY_DOWN:
                self.ymove_ = 1
                self.keyindex[self.DOWN_KEY] = self.KEY_UP
            else:
                self.ymove_=0
                self.keyindex[self.DOWN_KEY] = self.KEY_UP

    def LoadImage(self):
        # 메인무기 이미지 로드
        if g_main_scroll == Unit.USAS:
            Unit.main_gun = load_image("resource/weapon/USAS_INGAME.png")
        elif g_main_scroll == Unit.AWP:
            Unit.main_gun = load_image("resource/weapon/AWP_INGAME.png")
        elif g_main_scroll == Unit.SCAR:
            Unit.main_gun = load_image("resource/weapon/SCAR_INGAME.png")
        elif g_main_scroll == Unit.M4:
            Unit.main_gun = load_image("resource/weapon/M4_INGAME.png")
        elif g_main_scroll == Unit.M16A1:
            Unit.main_gun = load_image("resource/weapon/USAS_INGAME.png")
        elif g_main_scroll == Unit.MP5:
            Unit.main_gun = load_image("resource/weapon/MP5_INGAME.png")
        elif g_main_scroll == Unit.UMP:
            Unit.main_gun = load_image("resource/weapon/UMP_INGAME.png")
            # 핸드건 이미지 로드
            #      if g_sub_scroll==Unit.ANACONDA:
            #          Unit.hand_gun=load_image("resource/weapon/ANACONDA_INGAME.png")
            #      elif g_sub_scroll==Unit.D_EAGLE:
            #          Unit.hand_gun=load_image("resource/weapon/D_EAGLE_INGAME.png")
            #      elif g_sub_scroll==Unit.GLOCK:
            #          Unit.hand_gun=load_image("resource/weapon/GLOCK_INGAME.png")

