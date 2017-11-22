from pico2d import *
class Font:
    def __init__(self):
        self.font = load_font('font.ttf', 40)

    def update(self):
            pass
    def draw(self):
        self.font.draw(0, 550, "Time : ", (255, 255, 255))
