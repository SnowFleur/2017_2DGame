from pico2d import *



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
        self.frame_ = 0
        self.x_=0
        if(Unit.image==None):
            Unit.image=load_image('resource/Unit/unit ani.png')
    def Draw(self):
        self.image.clip_draw(self.frame_ * 99, 100, 90, 500, 100+self.x_, 100)
        self.frame = (self.frame_ + 1) % 8
        self.x_+=1
    def UnitControl(self):  #유닛 컨트롤
        pass



open_canvas()
running = True
unit=Unit() # Unit 객체 생성
map=Map() #맵 객체 생성
while ( running):
    clear_canvas()
    map.Draw() #맵 생성

    #unit.draw()
    update_canvas()
    delay(0.05)
close_canvas()
