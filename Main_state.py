from pico2d import *
import game_framework

xmove,ymove=0,0
class Map:
    #상수 매크로 정의
    FIRST_MAP,SECOND_MAP=1,2
    def __init__(self):  #생성과 동시에 두개의 맵 이미지 로드
        self.selectmap_=self.FIRST_MAP # 임시로 첫번쨰 맵만 로딩
        self.firstmap_=load_image('resource/map/map1.png')
        self.secondmap_ = load_image('resource/map/map2.png')
    def Draw(self):  #상수 매크로 에 따른 맵 그리기
        if(self.selectmap_==self.FIRST_MAP):
            self.firstmap_.draw(400,300)
        elif(self.selectmap_==self.SECOND_MAP_MAP):
            self.secondmap_.draw(400,300)



class Unit:
    image = None
    def __init__(self):
        self.frame_ = 1
        self.xpos_,self.ypos_=100,100
        if(Unit.image==None):
            Unit.image=load_image('resource/Unit/unit ani.png')
    def Draw(self):    #Left,Bottom,가로길이,세로길이,x,y,
                        # Bottom은 실질적인 이미지 크기 인거 같음
                        #1. 가로 , 2. 세로,가로넓이,세로넓이,
        #self.image.clip_draw(self.frame_*70, 200, 50, 50, 100, 100)
        self.ypos_+=ymove
        self.xpos_ += xmove
        self.image.clip_draw(0,550, 50, 50, self.xpos_, self.ypos_)
        self.frame_ += 1

        # angle,x,y,가로크기,세로크기
        #self.image.rotate_clip.draw(0,56,200,100,100,100,100)
        #self.image.rotate_draw(56,200,100,100,100)

    # self.image.clip_draw(self.frame_ * 70, 100, 70, 500, 170, 100)
       # self.frame_ = self.frame_ % 8

    def UnitControl(self):  #유닛 컨트롤
        events = get_events()
        for event in events:
            if (event.type == SDL_KEYDOWN) == (event.key == SDLK_w):  # 앞(세로+)
                 self.ypos_+=1
            elif event.type == SDL_KEYUP and event.key == SDLK_w:  # 앞(세로+)
                pass



def enter():
    global unit,map
    open_canvas()
    unit = Unit()  # Unit 객체 생성
    map = Map()  # 맵 객체 생성

def exit():
    global unit,map
    del (unit)
    del (map)
    close_canvas()

def update():
    pass
def draw():
    clear_canvas()
    map.Draw() #맵 생성
#    unit.UnitControl()

    unit.Draw()

    delay(0.085)
    update_canvas()


def handle_events():
    global ymove,xmove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type==SDL_KEYDOWN and event.key ==SDLK_w: # 위
                ymove+=4
        elif event.type == SDL_KEYUP and event.key == SDLK_w:
                ymove = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_s: #아래
            ymove -= 4
        elif event.type == SDL_KEYUP and event.key == SDLK_s:
            ymove = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_a: # 왼쪽
            xmove -= 4
        elif event.type == SDL_KEYUP and event.key == SDLK_a:
            xmove = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_d:  #오른쪽
           xmove += 4
        elif event.type == SDL_KEYUP and event.key == SDLK_d:
            xmove = 0


def pause():
    pass


def resume():
    pass






