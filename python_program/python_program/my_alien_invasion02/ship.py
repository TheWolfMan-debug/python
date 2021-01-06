import pygame
from pygame.sprite import Sprite
import random
import os


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.ship_type()

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        


    def update(self):
        """更新移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor

        # 根据self.center 更新rect对象 但只存储center 的整数部分
        self.rect.x = self.x
        self.rect.y = self.y
        self.update_center()


    def ship_type(self):
        # 获取随机数
        self.ship_random = self.ai_settings.ship_random
        my_path = "ship" + str(self.ship_random) + ".png"
        fre_path = "E:\python_program\python_program\my_alien_invasion02\images\ships"
        total_path = os.path.join(fre_path,my_path)
        self.image = pygame.image.load(total_path)

        # 加载飞船图像并获取器外接矩形
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 在飞船的属性center 中存储小数值
        self.x = float(self.screen_rect.centerx)
        self.y = float(self.screen_rect.bottom-self.rect.height)
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.x = float(self.screen_rect.centerx)
        self.y = float(self.screen_rect.bottom-self.rect.height)

    def update_center(self):
        self.ai_settings.ship_centerx = self.rect.centerx
        
