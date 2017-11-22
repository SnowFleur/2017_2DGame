from pico2d import *

#***************************
#AI클래스
#***************************
class Ai:
    image = None
    AI_MOVE,AI_ATTACK=0,1
    def __init__(self):
        self.xmove, self.ymove = 0, 0
        self.xpos_, self.ypos_ = 100, 500
        self.rotate_=0
        self.hp_ = 100  # 유닛 HP 계수
        self.shild = _ = 100  # 유닛 실드
        self.keyindex = [False, False, False, False]
        if (Ai.image == None):
            Ai.image = load_image('resource/Main_Resource/AI_INGAME.png')
    def Draw(self):  # Left,Bottom,가로길이,세로길이,x,y,
        self.ypos_ += self.ymove
        self.xpos_ += self.xmove
        self.image.rotate_draw(self.rotate_, self.xpos_, self.ypos_)
    def AiAttack(self):
        pass
    def AiMove(self):
        pass
    def ReturnBox(self):
        return self.xpos_ - 10, self.xpos_ + 10, self.ypos_ + 10, self.ypos_ - 10

  #  handle_state = {
     #   AI_ATTACK : AiAttack(),
    #     AI_MOVE:AiMove(),
    #    }


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)




