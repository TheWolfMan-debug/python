import pygame


class Platform(object):
    def __init__(self, screen, ai_settings):
        # 初始化
        self.screen_rect = screen.get_rect()
        self.color = (0,255,0)
        self.ai_settings = ai_settings
        self.screen = screen
        # 设置平台
        self.platform_rect = pygame.Rect(
            0, 0, ai_settings.platform_width, ai_settings.platform_height)
        self.platform_rect.centerx = screen.get_rect().centerx
        self.platform_rect.centery = screen.get_rect().bottom

        # 在平台的属性center 中存储小数值
        self.center = float(self.platform_rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """更具移动标志调整飞船的位置"""
        if self.moving_right and self.platform_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.platform_speed_factor
        if self.moving_left and self.platform_rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.platform_speed_factor
        
        # 根据self.center 更新rect对象 但只存储center 的整数部分
        self.platform_rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制平台"""
        pygame.draw.rect(self.screen,self.color,self.platform_rect)
