import pygame
from settings import Settings
from my_platform import Platform
import random
from time import sleep


def check_events(my_platform):
    # 遍历事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出事件后退出程序
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            elif event.key == pygame.K_LEFT:
                my_platform.moving_left = True
            elif event.key == pygame.K_RIGHT:
                my_platform.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_platform.moving_left = False
            elif event.key == pygame.K_RIGHT:
                my_platform.moving_right = False


def ball_changing(ai_settings):
    # 改变小球的位置
    ai_settings.x += ai_settings.vx
    ai_settings.y += ai_settings.vy

    # 到达侧面则是其竖直速度反向
    if ai_settings.y >= ai_settings.WINDOW_H or ai_settings.y <= 0:
        ai_settings.vy = -ai_settings.vy
    # 到达地面则是其竖直速度反向
    if ai_settings.x >= ai_settings.WINDOW_W or ai_settings.x <= 0:
        ai_settings.vx = -ai_settings.vx


def platform_hit():
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_screen(screen, ai_settings, my_platform, clock):
    # 将背景图画上去(0,0,0)为RGB颜色
    screen.fill((0, 0, 0))
    # 根据球的坐标画圆
    pygame.draw.circle(screen, (255, 0, 0), (int(
        ai_settings.x), int(ai_settings.y)), 10)
    # 画平台
    my_platform.blitme()
    # 刷新画面
    pygame.display.update()
    # 控制游戏循环频率
    clock.tick(ai_settings.clock)
