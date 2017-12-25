from pico2d import *
from Title_state import *
from math import *
import Map_Class
import Main_state

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

    main_gun,hand_gun=None,None  #유닛 이미지
#    shot_effet[2]={None,None}
    KEY_DOWN,KEY_UP=True,False
    LEFT_KEY,RIGHT_KEY,UP_KEY,DOWN_KEY=0,1,2,3
    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.xmove_,self.ymove_=0,0    #키보드 연속 입력처리를 위한 변수
        self.xpos_,self.ypos_=100,100 # 실질적인 객체 위치 값
        self.rotate_=0 # 마우스 위치에 따른 객체 회전
        self.hp_=100 #유닛 HP 계수
        self.shild=_=100 #유닛 실드
        self.keyindex=[False,False,False,False] #키보드 인덱스
        if(Unit.main_gun==None):
            self.LoadImage()
    #스크롤링 추가#
    def SetBackground(self, bg):
        self.bg = bg
        #일종의 초기값
        self.xpos_ = 400
        self.ypos_ = 300

    def Draw(self):    #캐릭터 그리기
        #스크롤링 변경
        x = Main_state.g_mouse_x+self.bg.window_left
        y = Main_state.g_mouse_y+self.bg.window_bottom
        self.rotate_=atan2(self.ypos_-y,self.xpos_-x)
        self.rotate_+= 90*3.14/180
        Unit.main_gun.rotate_draw(self.rotate_, self.xpos_ - self.bg.window_left,self.ypos_ - self.bg.window_bottom)
    def UpDate(self, frame_time):  # 마우스 가 바라보는 방향에 따라 이미지 회전 함수
        distance = Unit.RUN_SPEED_PPS * frame_time  #속도
        self.ypos_ += (self.ymove_*distance)       #속도에 따른 X,Y값증가
        self.xpos_ += (self.xmove_*distance)
        #플레이어 맵 크기 만큼 이동 제한
        self.xpos_ = clamp(50, self.xpos_, self.bg.w-50)
        self.ypos_ = clamp(50, self.ypos_, self.bg.h-50)
    def ReturnRotate(self):   #현재 캐릭터가 바라보는 각도를 반환 해주는 함수
        return self.rotate_
    def ReturnPositon(self): #현재 캐릭터의 위치를 반환 해주는 함수
        return self.xpos_,self.ypos_
    def ReturnCameraPosition(self): #카메라 값 반환
        camera_x=self.bg.window_left
        camera_y=self.bg.window_bottom
        return camera_x,camera_x+800,camera_y+600,camera_y

    def UnitControl(self, event):  # 전체적인 유닛 컨트롤
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_a): #왼쪽 이동
            self.xmove_=-1
            print("왼쪽")
            self.keyindex[self.LEFT_KEY]=self.KEY_DOWN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):  # 오른쪽 이동
            self.xmove_= 1
            print("오른쪽")
            self.keyindex[self.RIGHT_KEY] = self.KEY_DOWN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):  # 위쪽 이동
                self.ymove_ = 1
                print("위쪽")
                self.keyindex[self.UP_KEY] = self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):  # 아래쪽 이동
                self.ymove_ = -1
                print("아래쪽")
                self.keyindex[self.DOWN_KEY] = self.KEY_DOWN
        if (event.type, event.key) == (SDL_KEYUP, SDLK_a):  # 왼쪽 업
            if self.keyindex[self.RIGHT_KEY]==self.KEY_DOWN:
                self.xmove_ = 1
                self.keyindex[self.LEFT_KEY]=self.KEY_UP
            else:
                self.xmove_=0
                self.keyindex[self.LEFT_KEY]=self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):  # 오른쪽 업
            if self.keyindex[self.LEFT_KEY] == self.KEY_DOWN:
                self.xmove_ = -1
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP
            else:
                self.xmove_=0
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_w):  # 윗키 업
            if self.keyindex[self.DOWN_KEY]==self.KEY_DOWN:
                self.ymove_ = -1
                self.keyindex[self.UP_KEY]=self.KEY_UP
            else:
                self.ymove_=0
                self.keyindex[self.UP_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_s):  # 아래키 업
            if self.keyindex[self.UP_KEY] == self.KEY_DOWN:
                self.ymove_ = 1
                self.keyindex[self.DOWN_KEY] = self.KEY_UP
            else:
                self.ymove_=0
                self.keyindex[self.DOWN_KEY] = self.KEY_UP

    def LoadImage(self):  # 타이틀 화면에서 선택한 무기의 이미지를 불러올 함수
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

