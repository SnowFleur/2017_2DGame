from pico2d import *
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

    image = None
    KEY_DOWN,KEY_UP=True,False
    LEFT_KEY,RIGHT_KEY,UP_KEY,DOWN_KEY=0,1,2,3
    def __init__(self):
        self.frame_ = 1
        self.xmove,self.ymove=0,0
        self.xpos_,self.ypos_=100,100
        self.keyindex=[False,False,False,False]
        if(Unit.image==None):
            Unit.image=load_image('resource/Unit/unit ani.png')
    def Draw(self):    #Left,Bottom,가로길이,세로길이,x,y,
                        # Bottom은 실질적인 이미지 크기 인거 같음
                        #1. 가로 , 2. 세로,가로넓이,세로넓이,
        #self.image.clip_draw(self.frame_*70, 200, 50, 50, 100, 100)
        self.ypos_+=self.ymove
        self.xpos_ +=self.xmove
        self.image.clip_draw(0,550, 50, 50, self.xpos_, self.ypos_)
        self.frame_ += 1

        # angle,x,y,가로크기,세로크기
        #self.image.rotate_clip.draw(0,56,200,100,100,100,100)
        #self.image.rotate_draw(56,200,100,100,100)

    # self.image.clip_draw(self.frame_ * 70, 100, 70, 500, 170, 100)
       # self.frame_ = self.frame_ % 8


    def UnitControl(self, event):
        if(event.type,event.key)==(SDL_KEYDOWN,SDLK_LEFT): #왼쪽 이동
            self.xmove=-5
            print("왼쪽")
            self.keyindex[self.LEFT_KEY]=self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):  # 오른쪽 이동
            self.xmove= 5
            print("오른쪽")
            self.keyindex[self.RIGHT_KEY] = self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):  # 위쪽 이동
                self.ymove = 5
                print("위쪽")
                self.keyindex[self.UP_KEY] = self.KEY_DOWN

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):  # 아래쪽 이동
                self.ymove = -5
                print("아래쪽")
                self.keyindex[self.DOWN_KEY] = self.KEY_DOWN
        if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):  # 왼쪽 업
            if self.keyindex[self.RIGHT_KEY]==self.KEY_DOWN:
                self.xmove = 5
                self.keyindex[self.LEFT_KEY]=self.KEY_UP
            else:
                self.xmove=0
                self.keyindex[self.LEFT_KEY]=self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):  # 오른쪽 업
            if self.keyindex[self.LEFT_KEY] == self.KEY_DOWN:
                self.xmove = -5
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP
            else:
                self.xmove=0
                self.keyindex[self.RIGHT_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):  # 윗키 업
            if self.keyindex[self.DOWN_KEY]==self.KEY_DOWN:
                self.ymove = -5
                self.keyindex[self.UP_KEY]=self.KEY_UP
            else:
                self.ymove=0
                self.keyindex[self.UP_KEY] = self.KEY_UP

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):  # 아래키 업
            if self.keyindex[self.UP_KEY] == self.KEY_DOWN:
                self.ymove = 5
                self.keyindex[self.DOWN_KEY] = self.KEY_UP
            else:
                self.ymove=0
                self.keyindex[self.DOWN_KEY] = self.KEY_UP