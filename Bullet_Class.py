import random
from pico2d import *
from math import *
import  Main_state
class Bullet:
    #상수  정의
    imag=None

    PIXEL_PER_METER=(10.0/0.3)  #10 pixel 30cm
    RUN_SPPED_KMPH=30.0   #시간당 20km
    RUN_SPEED_MPH=(RUN_SPPED_KMPH*1000.0/60.0)
    RUN_SPEED_MPS=(RUN_SPEED_MPH/60.0)
    RUN_SPEED_PPS=(RUN_SPEED_MPS* PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    REBOUND_MINUS,REBOUND_PLUS=0,1
    #사운드
    shot_sound=None
    drop_sound=None
    def __init__(self):
        self.xpos_,self.ypos_=0,0
        self.xmove_,self.ymove_=0,0
        ###스크롤링 추가 내용
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Bullet.shot_sound == None:  #총쏘는 소리
            Bullet.shot_sound = load_music('resource/sound/cut1.mp3')
            Bullet.shot_sound.set_volume(300)
            Bullet.drop_sound=load_music('resource/sound/7.62shell3.mp3')
            Bullet.drop_sound.set_volume(23)
        self.rotate_=0
        self.sound_count=0
        self.rebound_=0 #반동
        self.rate_time=0 #이걸 주지 않으면 너무 많은 이미지가 한꺼번에 나감
        if Bullet.imag==None:
            Bullet.imag=load_image("resource/Main_Resource/Bullet.png")
    def Draw(self):
        self.sound_count+=self.sound_count
        print(self.sound_count)
        if(self.sound_count>10000000000000000000):
            print("탄피",self.sound_count)
            self.drop_sound.play()
            self.sound_count=0
        Bullet.imag.rotate_draw(self.rotate_,self.xpos_-self.bg.window_left,
                                self.ypos_- self.bg.window_bottom,50,70)
    def Update(self, frame_time):
        distance = Bullet.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.ymove_ * distance)
        self.xpos_ += (self.xmove_ * distance)
        ####스크롤링 추가###
        self.bg.window_left = 0
        self.bg.window_bottom = 0
    def Shot(self):
        self.ymove_=cos(self.rotate_)*10
        self.xmove_=  - sin(self.rotate_)*10
        self.shot_sound.play()
       # self.sound_count=1

    def UnitPosition(self,xpos,ypos,rotate):
        self.xpos_=xpos
        self.ypos_=ypos
        self.rotate_=rotate
        ####스크롤링 추가###
    def SetBackground(self, bg):
        self.bg = bg
        self.xpos_ = self.bg.w / 2
        self.ypos_ = self.bg.h / 2

    def RateShot(self,rebound):  #연속 발사
        self.rebound_=rebound
        self.rate_time+=1
        if self.rate_time>25:
            dir= random.randint(Bullet.REBOUND_MINUS,Bullet.REBOUND_PLUS)
            self.shot_sound.play()
         #   self.sound_count=1


            if dir==Bullet.REBOUND_PLUS:
                self.ymove_ = cos(self.rotate_) * 10
                self.xmove_ = - sin(self.rotate_) * 10 + self.rebound_
            if dir==Bullet.REBOUND_MINUS:
                self.ymove_ = cos(self.rotate_) * 10
                self.xmove_ = - sin(self.rotate_) * 10 - self.rebound_

            # +,- 왼쪽
            # +,+ 오른쪽

            self.rate_time=0

            return True



class Shell:
    image=None
    drop_sound = None

    def __init__(self):
        self.xpos_,self.ypos_=0,0  # 탄피 위치
        self.rotate_=0  # 회전 값
        self.shot_=0 #총알 솼는지 여부 단위
        self.time_= random.randint(100,200) #탄피 회전 시간
        self.remove_time_=0 #탄피 사라질 시간
        ###스크롤링 추가 내용
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Shell.drop_sound == None:  # 총쏘는 소리
            Shell.drop_sound=load_music('resource/sound/7.62Shell3.mp3')
            Shell.drop_sound.set_volume(32)
        if Shell.image==None:
            Shell.image= load_image("resource/Main_Resource/shell.png")
    def Darw(self):

        Shell.image.rotate_draw(self.rotate_, self.xpos_ - self.bg.window_left,
                                self.ypos_ - self.bg.window_bottom, 25, 50)
    def Update(self, frame_time):

        distance =  (self.time_/10)* frame_time
        self.rotate_ += (self.shot_ * distance)
        if self.time_>0 and self.shot_==1:
            self.time_= self.time_-1


        #스클롤링 추가#
        self.bg.window_left = 0
        self.bg.window_bottom = 0
       ####스크롤링 추가###
    def SetBackground(self, bg):
        self.bg = bg
        self.xpos_ = self.bg.w / 2
        self.ypos_ = self.bg.h / 2

    def InputPosition(self,xpos,ypos):
        self.xpos_,self.ypos_=xpos,ypos
        self.shot_=1








