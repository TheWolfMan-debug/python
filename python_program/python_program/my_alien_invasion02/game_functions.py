import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from ship import Ship
import os
import tkinter.messagebox
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *
import time
import threading
import random


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    # pygame.key.set_repeat(10,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN or pygame.key.set_repeat(5, 50):
            check_keydown_events(
                event, ai_settings, screen, stats,  sb, ship, aliens, play_button, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb,
                              play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮式开始新游戏"""
    game_button_clicked = play_button.play_rect.collidepoint(mouse_x, mouse_y)
    new_game_button_clicked = play_button.play_new_game_rect.collidepoint(
        mouse_x, mouse_y)
    quit_game_button_clicked = play_button.quit_game_rect.collidepoint(
        mouse_x, mouse_y)
    help_game_button_clicked = play_button.help_game_rect.collidepoint(
        mouse_x, mouse_y)
    # 如果游戏没有运行
    if not stats.game_active:
        # 点击开始游戏
        if game_button_clicked:
            initialize_game_settings(
                ai_settings, stats, sb, aliens, bullets, screen, ship)
        # 点击开始新游戏
        elif new_game_button_clicked:
            if os.path.exists(stats.filename):
                os.remove(stats.filename)
            stats.initial_high_score()
            initialize_game_settings(
                ai_settings, stats, sb, aliens, bullets, screen, ship)
        # 点击退出游戏
        elif quit_game_button_clicked:
            sys.exit()
        # 点击帮助
        elif help_game_button_clicked:
            help_document(stats)


def help_document(stats):

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('Help documentation')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300+375+150')  # 这里的乘是小x

    window.resizable(0, 0)  # 防止用户调整尺寸

    filename = stats.help_filename
    f_open = open(filename)
    content = f_open.read()
    f_open.close()
    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text=content, bg="lightgreen", justify=LEFT,
                 font=('Arial', 12), width=60, height=25)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    # 第5步，放置标签
    # l.place(rely=1, relx=0.5, x=-150, y=-150)    # Label内容content区域放置位置，自动调节尺寸
    l.pack()
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    # 第6步，主窗口循环显示
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环

def game_pause(stats):
        # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('Note')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('200x100+535+200')  # 这里的乘是小x

    window.resizable(0, 0)  # 防止用户调整尺寸

    filename = stats.game_pause_filename
    f_open = open(filename)
    content = f_open.read()
    f_open.close()
    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text=content, bg="lightgreen", justify=LEFT,
                 font=('Arial', 12), width=60, height=25)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    # 第5步，放置标签
    # l.place(rely=1, relx=0.5, x=-150, y=-150)    # Label内容content区域放置位置，自动调节尺寸
    l.pack()
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    # 第6步，主窗口循环显示
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环



def initialize_game_settings(ai_settings, stats, sb, aliens, bullets, screen, ship):
    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()
    ai_settings.image_change += 1
    if ai_settings.image_change != 1:
        # 改变飞船的型号
        ship.ship_type()
    ship.update_center()


    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    
    sb.prep_alien_number()

    if ai_settings.image_change != 1:
        sb.prep_ships()

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一个外星人，并让飞船居中
    create_alien(ai_settings, screen, aliens, stats)

    ship.center_ship()


def check_keydown_events(event, ai_settings, screen, stats,  sb, ship, aliens, play_button, bullets):
    if event.key == pygame.K_RIGHT:
        # 使飞船持续移动的标志为真
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 使飞船持续移动的标志为真
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        update_shoots(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        # 退出游戏
        sys.exit()
    elif event.key == pygame.K_s and not stats.game_active:
        # 开始游戏
        initialize_game_settings(
            ai_settings, stats, sb, aliens, bullets, screen, ship)
    elif event.key == pygame.K_n and not stats.game_active:
        # 开始新游戏
        if os.path.exists(stats.filename):
            os.remove(stats.filename)
        stats.initial_high_score()
        initialize_game_settings(
            ai_settings, stats, sb, aliens, bullets, screen, ship)
    elif event.key == pygame.K_h and not stats.game_active:
        # 帮助文档
        help_document(stats)
    elif event.key == pygame.K_p and stats.game_active:
        game_pause(stats)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 使飞船持续移动的标志为假
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 使飞船持续移动的标志为假
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def create_alien(ai_settings, screen, aliens, stats):
    """创建一个外星人并将其加入当前行"""
    for i in range(stats.alien_number):
        alien = Alien(ai_settings, screen)
        aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges() == 1:
            alien.fleet_direction_x *= -1
        elif alien.check_edges() == 2:
            alien.fleet_direction_y *= -1


def check_mutual_collision(aliens):
    alien_i = 0
    while alien_i < len(aliens.sprites())-1:
        alien_j = alien_i + 1
        while alien_j < len(aliens.sprites()):
            if pygame.sprite.collide_mask(aliens.sprites()[alien_i], aliens.sprites()[alien_j]):
                aliens.sprites()[alien_i].fleet_direction_x *= -1
                aliens.sprites()[alien_j].fleet_direction_y *= -1
            alien_j += 1
        alien_i += 1


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 检查是否有子弹击中了敌人
    # 如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
    check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹
        bullets.empty()
        # 加快游戏节奏
        ai_settings.increase_speed()
        # 提升等级
        stats.level += 1

        if stats.level % 3 == 0:
            stats.alien_number += 1
            sb.prep_alien_number()
        sb.prep_level()
        # 创建一个外星人
        create_alien(ai_settings, screen, aliens, stats)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """响应被外星人撞到的"""
    if stats.ships_left - 1 > 0:
        # 将ship_left 减一
        stats.ships_left -= 1

        # 更新记分牌
        ship.ship_type()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一个新的外星人，并将飞船放到屏幕低端中央
        create_alien(ai_settings, screen, aliens, stats)
        ship.center_ship()

        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        # 更新文件中的最高分
        f_open = open(stats.filename, "w")
        f_open.write(str(stats.score))
        f_open.close()


def update_shoots(bullets, ai_settings, screen, ship):
    """使子弹持续射击"""
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def update_screen(ai_settings, screen, stats,  sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 重绘飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    

    # 让最近绘制的屏幕可见
    pygame.display.flip()

    # 记录界面刷新次数
    ai_settings.screen_number += 1
    # 绘制帮助文档
    if (ai_settings.screen_number == 1):
        help_document(stats)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    # 检查是否外星人之间发生碰撞
    check_mutual_collision(aliens)
    # 更新外星人群中所有外星人的位置
    aliens.update()
    # 是否处于无敌状态
    if not ai_settings.ship_invincible:
        if pygame.sprite.spritecollideany(ship, aliens):
            # 监测外星人与飞船之间的碰撞
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 更新子弹状态
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中了敌人
    # 如果是这样，就删除相应的子弹和外星人
    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)
