from pico2d import *
from math import *
import random
#***************************
#AI클래스
#***************************
class Ai:
    image = None
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30cm
    RUN_SPPED_KMPH = 20.0  # 시간당 20km
    RUN_SPEED_MPH = (RUN_SPPED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    AI_MOVE,AI_ATTACK,=0,1


    def __init__(self):
        self.xmove_, self.ymove_ = 0, 0
        self.xpos_, self.ypos_ = 150, 475
        self.rotate_=0
        self.hp_ = 100  # 유닛 HP 계수
        self.shild_ = _ = 100  # 유닛 실드
        self.state_=0
        self.dis_vector=[random.randint(0,1),random.randint(0,1)]
        self.keyindex = [False, False, False, False]
        if (Ai.image == None):
            Ai.image = load_image('resource/Main_Resource/AI_INGAME.png')
    def Draw(self):  # Left,Bottom,가로길이,세로길이,x,y,

        self.image.rotate_draw(self.rotate_, self.xpos_, self.ypos_)
    def UpDate(self, frame_time):
        self.handle_state[self.state_](self)
        distance = Ai.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.ymove_ * distance)
        self.xpos_ += (self.xmove_ * distance)
    def AiAttack(self):
        pass
    def AiMove(self):
        self.rotate_ = atan2(-(750 - self.xpos_), (575 - self.ypos_))
        if self.xpos_<750:
            self.xmove_=1
        else:
            self.xmove_=0

        pass
    def ReturnBox(self):
        return self.xpos_ -150, self.xpos_ + 150, self.ypos_ + 125, self.ypos_ - 125


    handle_state = {   # AI 핸들 컨트롤러
            AI_ATTACK: AiAttack,
            AI_MOVE: AiMove,
                   }

    move_state = {   # AI 이동 핸들러
            AI_ATTACK: AiAttack,
            AI_MOVE: AiMove,
                   }


