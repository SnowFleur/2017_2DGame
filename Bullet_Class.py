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


    def __init__(self):
        self.xpos_,self.ypos_=0,0
        self.xmove_,self.ymove_=0,0
        self.rotate_=0
        if Bullet.imag==None:
            Bullet.imag=load_image("resource/Main_Resource/Bullet.png")
    def Draw(self):  #상수 매크로 에 따른 맵 그리기
        Bullet.imag.rotate_draw(self.rotate_,self.xpos_,self.ypos_,50,70)
    def Update(self, frame_time):
        distance = Bullet.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.ymove_ * distance)
        self.xpos_ += (self.xmove_ * distance)
    def Shot(self):
        self.rotate_=atan2( -(Main_state.g_mouse_x-self.xpos_) ,( Main_state.g_mouse_y-self.ypos_ ))
        ax=cos(self.rotate_)
        ay=sin(self.rotate_)

     #   ax=Main_state.g_mouse_x-self.xpos_
     #   ay=Main_state.g_mouse_y-self.ypos_
     #   m=ax/ay
        self.ymove_=ax
        self.xmove_=-ay
    def UnitPosition(self,xpos,ypos):
        self.xpos_=xpos
        self.ypos_=ypos









