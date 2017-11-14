from pico2d import *

#***************************
#AI클래스
#***************************
class Ai:
    class Unit:
        image = None
        AI_MOVE,AI_ATTACK=0,1
        def __init__(self):
            self.frame_ = 1
            self.xmove, self.ymove = 0, 0
            self.xpos_, self.ypos_ = 100, 500
            self.keyindex = [False, False, False, False]
            if (Ai.image == None):
                Ai.image = load_image('resource/Unit/unit ani.png')
        def Draw(self):  # Left,Bottom,가로길이,세로길이,x,y,
            self.ypos_ += self.ymove
            self.xpos_ += self.xmove
            self.image.clip_draw(0, 550, 50, 50, self.xpos_, self.ypos_)
            self.frame_ += 1
        def AiAttack(self):
            pass
        def AiMove(self):
            pass

        handle_state = {
            AI_ATTACK : AiAttack(),
            AI_MOVE:AiMove(),
        }
        def update(self):
            self.frame = (self.frame + 1) % 8
            self.handle_state[self.state](self)

