from pico2d import *

class Map:
    #상수 매크로 정의
    FIRST_MAP,SECOND_MAP=1,2
    def __init__(self):  #생성과 동시에 두개의 맵 이미지 로드
        self.selectmap_=self.SECOND_MAP # 임시로 첫번쨰 맵만 로딩
        self.firstmap_=load_image('resource/map/map3.png')
        self.secondmap_ = load_image('resource/map/map3.png')

    def Draw(self):  #상수 매크로 에 따른 맵 그리기
        if(self.selectmap_==self.FIRST_MAP):
            self.firstmap_.draw(640,360)
        elif(self.selectmap_==self.SECOND_MAP):
            self.secondmap_.draw(640,360)
