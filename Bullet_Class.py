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

    def __init__(self):
        self.xpos_,self.ypos_=0,0
        self.xmove_,self.ymove_=0,0
        self.rotate_=0
        self.rebound_=0 #반동
        self.rate_time=0 #이걸 주지 않으면 너무 많은 이미지가 한꺼번에 나감
        if Bullet.imag==None:
            Bullet.imag=load_image("resource/Main_Resource/Bullet.png")
    def Draw(self):  #상수 매크로 에 따른 맵 그리기
        Bullet.imag.rotate_draw(self.rotate_,self.xpos_,self.ypos_,50,70)
    def Update(self, frame_time):
        distance = Bullet.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.ymove_ * distance)
        self.xpos_ += (self.xmove_ * distance)
    def Shot(self):
        self.ymove_=cos(self.rotate_)*10
        self.xmove_=  - sin(self.rotate_)*10
    def UnitPosition(self,xpos,ypos,rotate):
        self.xpos_=xpos
        self.ypos_=ypos
        self.rotate_=rotate
    def RateShot(self,rebound):  #연속 발사
        self.rebound_=rebound
        self.rate_time+=1
        if self.rate_time>25:
            dir= random.randint(Bullet.REBOUND_MINUS,Bullet.REBOUND_PLUS)
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
    def __init__(self):
        self.xpos_,self.ypos_=0,0  # 탄피 위치
        self.rotate_=0  # 회전 값
        self.shot_=0 #총알 솼는지 여부 단위
        self.time_= random.randint(100,200) #탄피 회전 시간
        self.remove_time_=0 #탄피 사라질 시간
        if Shell.image==None:
            Shell.image= load_image("resource/Main_Resource/shell.png")
    def Darw(self):
        Shell.image.rotate_draw(self.rotate_, self.xpos_, self.ypos_, 25, 50)
    def Update(self, frame_time):
        distance =  (self.time_/10)* frame_time
        self.rotate_ += (self.shot_ * distance)
        if self.time_>0 and self.shot_==1:
            self.time_= self.time_-1


    def InputPosition(self,xpos,ypos):
        self.xpos_,self.ypos_=xpos,ypos
        self.shot_=1








