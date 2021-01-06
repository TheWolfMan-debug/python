import pygame
from pygame.sprite import Sprite
import random
import os


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, aisettings, screen):
        """初始化外星人的类"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = aisettings


        # 获取随机数
        self.alien_random = random.randint(1,16)
        # self.alien_random = random.randint(11,13)
        # self.alien_random = 10

        # 加载外星人图像，并设置其rect属性
        my_path = "alien" + str(self.alien_random) + ".png"
        # fre_path = r"E:\python_program\python_program\my_alien_invasion03\images\aliens"
        fre_path = self.ai_settings.current_file_path + r"\images\aliens"
        total_path = os.path.join(fre_path,my_path)
        self.image = pygame.image.load(total_path)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = random.randint(100, self.ai_settings.screen_width-100)
        self.rect.y = random.randint(50, self.ai_settings.screen_height-200)

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 控制外星人的速度
        self.vx = self.ai_settings.alien_vx
        self.vy = self.ai_settings.alien_vy
        

        # fleet_direction为速度方向标志
        self.fleet_direction_x = random.randint(-1,1)
        while self.fleet_direction_x==0:
            self.fleet_direction_x = random.randint(-1,1)
        self.fleet_direction_y = random.randint(-1,1)
        while self.fleet_direction_y==0:
            self.fleet_direction_y = random.randint(-1,1)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向右移动外星人"""
        self.x += (self.vx * self.fleet_direction_x)
        self.rect.x = self.x
        self.y += (self.vy * self.fleet_direction_y)
        self.rect.y = self.y

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left):
            return 1
        elif (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= screen_rect.top):
            return 2
