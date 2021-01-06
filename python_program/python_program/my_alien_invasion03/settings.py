import random
import math
import os


class Settings(object):
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 获取当前文件目录
        self.current_file_path = os.getcwd()

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.fullscreen = 0

        # 飞船的设置
        # 飞船数量限制
        self.ship_limit = 3
        # 飞船是否无敌
        self.ship_invincible = False

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        
        self.bullets_allowed = 1000

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数提高
        self.score_scale = 1.5

        # 初始化生成外星人的数量
        self.alien_number = 5

        # 飞船的中心坐标
        self.ship_centerx = 0

        # 飞船图像是否改变
        self.image_change = 0
        # 是否出现文档
        self.screen_number = 0

        self.initialize_dynamic_settings()

        # 音效设置
        self.music_flag = 1


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 1.2
        self.ship_random = random.randint(1, 18)

        # 一个外星人的分数
        self.alien_points = 20

        # 控制外星人的速度
        self.alien_vx = random.randint(12, 15)/10
        # 控制外星人y方向速度
        self.alien_vy = random.randint(9, 12)/10

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_vy *= self.speedup_scale
        self.alien_vx *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
