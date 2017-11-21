from pico2d import *
from Class import *
from Title_state import *
import game_framework


class Gun:
    #상수 매크로 정의
    USAS,AWP,SCAR,M4,M16A1,MP5,UMP=0,150,300,450,600,750,900
    ANACONDA,D_EAGLE,GLOCK=0,150,300
    main_gun,hand_gun=None,None
    def __init__(self):  #생성과 동시에 두개의 맵 이미지 로드
        self.xpos_,self.ypos_=107,130 #x,y 좌표
        self.r_=0 #마우스 위치에 따른  총 회전
        self.LoadImage()

    def LoadImage(self):
        #메인무기 이미지 로드
        if g_main_scroll==Gun.USAS:
            Gun.main_gun=load_image("resource/weapon/USAS_INGAME.png")
        elif g_main_scroll==Gun.AWP:
            Gun.main_gun=load_image("resource/weapon/AWP_INGAME.png")
        elif g_main_scroll==Gun.SCAR:
            Gun.main_gun=load_image("resource/weapon/SCAR_INGAME.png")
        elif g_main_scroll==Gun.M4:
            Gun.main_gun=load_image("resource/weapon/M4_INGAME.png")
        elif g_main_scroll==Gun.M16A1:
            Gun.main_gun=load_image("resource/weapon/USAS_INGAME.png")
        elif g_main_scroll==Gun.MP5:
            Gun.main_gun=load_image("resource/weapon/MP5_INGAME.png")
        elif g_main_scroll==Gun.UMP:
            Gun.main_gun=load_image("resource/weapon/UMP_INGAME.png")
        #핸드건 이미지 로드
  #      if g_sub_scroll==Gun.ANACONDA:
  #          Gun.hand_gun=load_image("resource/weapon/ANACONDA_INGAME.png")
  #      elif g_sub_scroll==Gun.D_EAGLE:
  #          Gun.hand_gun=load_image("resource/weapon/D_EAGLE_INGAME.png")
  #      elif g_sub_scroll==Gun.GLOCK:
  #          Gun.hand_gun=load_image("resource/weapon/GLOCK_INGAME.png")



    def Draw(self):  #상수 매크로 에 따른 무기 호출
        Gun.main_gun.draw(self.xpos_,self.ypos_)


