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
        self.shild_  = 100  # 유닛 실드
        self.state_=0
        self.dis_vector=[random.randint(-1,1),random.randint(-1,1)]
        self.leftvector=[0,0]
        self.rightvector=[0,0]
        self.keyindex = [False, False, False, False]
        if (Ai.image == None):
            Ai.image = load_image('resource/Main_Resource/AI_INGAME.png')
    def Draw(self):  # Left,Bottom,가로길이,세로길이,x,y,
        def VectorDotProduc():
            self.leftvector[0] = 50*sin(self.rotate_-0.523)+ self.xpos_
            self.leftvector[1] = 50*cos(self.rotate_-0.523) + self.ypos_

            self.rightvector[0] = 50 * sin(self.rotate_ +0.523) + self.xpos_
            self.rightvector[1] = 50 * cos(self.rotate_ + 0.523) + self.ypos_

        VectorDotProduc()
        self.image.rotate_draw(self.rotate_, self.xpos_, self.ypos_)
        temp_x = (self.xpos_ + self.dis_vector[0] * 100)
        temp_y = 600-(self.ypos_ + self.dis_vector[1] * 100)

        temp_x2 = self.xpos_
        temp_y2 = 600-self.ypos_

        temp_y3=600-self.leftvector[1]
        temp_y4=600-self.rightvector[1]

#        Draw_Line(int(temp_x2), int(temp_y2), int(temp_x), int(temp_y))
#        Draw_Line(int(temp_x2), int(temp_y2), int(self.leftvector[0]), int(temp_y3))
#        Draw_Line(int(temp_x2), int(temp_y2), int(self.rightvector[0]), int(temp_y4))


    def UpDate(self, frame_time):
        self.handle_state[self.state_](self)
        distance = Ai.RUN_SPEED_PPS * frame_time
        self.ypos_ += (self.dis_vector[1] * distance)
        self.xpos_ += (self.dis_vector[0] * distance)

    def AiAttack(self):
        pass


        pass
    def AiMove(self):

#        self.rotate_ = atan2((self.ypos_-self.dis_vector[1]*100) - self.ypos_), ((self.ypos_-self.dis_vector[1]*100) - self.xpos_))
        self.rotate_ += -90 * 3.14 / 180

        if(self.xpos_>800):
            self.dis_vector = [random.randint(-1, 0), random.randint(-1, 1)]
        if (self.xpos_< 0):
            self.dis_vector = [random.randint(0, 1), random.randint(-1, 1)]
        if (self.ypos_ > 600):
                self.dis_vector = [random.randint(-1, 1), random.randint(-1, 0)]
        if (self.ypos_ < 0):
                self.dis_vector = [random.randint(-1, 1), random.randint(0, 1)]
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


