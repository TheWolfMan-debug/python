import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from music import Music
import os


def run_game():
    # 初始化游戏并创建一个屏幕对象 初始化pygame、设置和屏幕对象
    pygame.init()


    # 设置窗口出现的位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (40, 55)

    # 初始化一个设置实例
    ai_settings = Settings()

    # 设置屏幕大小
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # # 设置屏幕大小(全屏)
    # screen = pygame.display.set_mode(
    #     (ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)

    # 设置标题
    pygame.display.set_caption("Thunder Fighters Vs Digital Monsters")

    #加载背景音乐
    my_music = Music(ai_settings)
    my_music.menu_music()

    # 创建Play按钮
    play_button = Button(ai_settings, screen)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # # 创建一个外星人
    # gf.create_alien(ai_settings, screen, aliens, stats)
 
    # 创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets,my_music)

        if stats.game_active:
            # 在更新屏幕之前调用飞船的方法
            ship.update()

            # 更新子弹状态
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets,my_music)

            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats,
                             sb, ship, aliens, bullets,my_music)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats,  sb,
                         ship, aliens, bullets, play_button)


if __name__ == "__main__":
    run_game()
