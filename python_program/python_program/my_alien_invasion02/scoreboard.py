import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """现实得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化现实得分设计的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.alien_number = self.stats.alien_number

        # 现实得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # 准备包含最高分和当前的分的图像
        self.prep_alien_number()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_high_score(self):
        """将最高分转换成渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Highest score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, None)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.alien_number_rect.top

    def prep_alien_number(self):
        """外星人当前的数量"""
        self.alien_number_image = self.font.render(
            "The number of Aliens: " + str(self.stats.alien_number), True, self.text_color, None)

        # 将外星人数量放置在右上角
        self.alien_number_rect = self.alien_number_image.get_rect()
        self.alien_number_rect.right = self.screen_rect.right - 20
        self.alien_number_rect.top = 20

    def prep_score(self):
        """将得分转换成一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: " + "{:,}".format(rounded_score)

        self.score_image = self.font.render(
            score_str, True, self.text_color, None)

        # 将得分放在外星人数量下面
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.alien_number_rect.right
        self.score_rect.top = self.alien_number_rect.bottom + 10


    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render(
            "Level: " + str(self.stats.level), True, self.text_color, None)

        # 将等级放在得分的下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        """现实还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left - 1):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上现实得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)
        self.screen.blit(self.alien_number_image,self.alien_number_rect)
