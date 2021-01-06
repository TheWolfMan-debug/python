import pygame
import random


class Settings(object):
    def __init__(self):
        # 窗体尺寸
        self.WINDOW_W, self.WINDOW_H = 640, 480
        # 球的坐标
        self.x, self.y = self.WINDOW_W/2, 10
        # 球在x,y方向上的速度
        self.vx, self.vy = 1, 1
        # self.vx, self.vy = random.randint(1,20)/10,random.randint(1,20)/10

        # 窗口出现的位置
        self.windows_position_x, self.windows_position_y = 350, 100

        # 设置平台生成的大小
        self.platform_width, self.platform_height = 50, 10

        # 设置平台移动的速度
        self.platform_speed_factor = 1.5

        # 控制游戏循环频率
        self.clock = 500
