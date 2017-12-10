from pico2d import *

class Map:
    #상수 매크로 정의
    FIRST_MAP,SECOND_MAP=1,2
    def __init__(self):  #생성과 동시에 두개의 맵 이미지 로드
        self.army_image = load_image('resource/map/army_map.png')
        self.city_map= load_image('resource/map/city_map.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.w = self.army_image.w
        self.h = self.army_image.h


    def set_center_object(self, player):
        self.center_object = player

    def Draw(self):
        self.army_image.clip_draw_to_origin(
        self.window_left, self.window_bottom,
        self.canvas_width, self.canvas_height,0, 0)

    def Update(self, frame_time):
        self.window_left = clamp(0,
                         int(self.center_object.xpos_) - self.canvas_width // 2,
                        self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                        int(self.center_object.ypos_) - self.canvas_height // 2,
                        self.h - self.canvas_height)

        def handle_event(self, event):
            pass
    def ReturnCenterXpos(self):
        return self.center_object.xpos_
    def ReturnCetnerYpos(self):
        return self.center_object.ypos_

  #  def Draw(self):  #상수 매크로 에 따른 맵 그리기
  #      if(self.selectmap_==self.FIRST_MAP):
  #          self.firstmap_.draw(640,360)
   #     elif(self.selectmap_==self.SECOND_MAP):
    #        self.secondmap_.draw(640,360)
