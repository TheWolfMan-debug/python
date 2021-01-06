import pygame
import os
import sys
from time import sleep
from settings import Settings
from my_platform import Platform
import game_functions as gf


def run_game():
    # 初始化pygame
    pygame.init()

    # 创建时钟对象 (可以控制游戏循环频率)
    clock = pygame.time.Clock()

    # 创建一个设置实例
    ai_settings = Settings()

    # 设置窗口出现的位置
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
        ai_settings.windows_position_x, ai_settings.windows_position_y)

    # 创建一个窗口
    screen = pygame.display.set_mode(
        (ai_settings.WINDOW_W, ai_settings.WINDOW_H), pygame.DOUBLEBUF, 32)

    # 设置窗口标题
    pygame.display.set_caption("hello,world!")

    # 创建一个平台实例
    my_platform = Platform(screen,ai_settings)

    # 游戏主循环
    while True:
        # 遍历事件
        gf.check_events(my_platform)

        # 跟新平台
        my_platform.update()

        # 记录小球的位置，速度变化
        gf.ball_changing(ai_settings)

        # 更新屏幕
        gf.update_screen(screen,ai_settings,my_platform,clock)
        

if __name__ == '__main__':
    run_game()