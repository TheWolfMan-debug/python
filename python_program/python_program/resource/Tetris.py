import pygame, sys
from pygame.locals import *
import random
import time
import copy


# 计算方块是否重叠
def algorithm(tetris, FixedBlock, equal):
    m = 0
    for judge_1 in range(0, len(tetris)):
        if equal == "equal":
            break
        i = 0
        for judge_2 in range(0, len(FixedBlock)):
            if equal == "equal":
                break
            z = 0
            for judge_3 in range(0, len(FixedBlock[i])):
                if (FixedBlock[i])[z] == tetris[m]:
                    equal = "equal"
                    break
                else:
                    z += 1
            i += 1
        m += 1
    return equal


# 判断是否有一排的情况，如果是，则输出eliminate(y轴为一排的值)
def eliminate(FixedBlock):
    list_a = []
    list_b = []
    for x_1 in FixedBlock:
        for x_2 in x_1:
            list_a.append(x_2)
    for y_1 in list_a:
        if y_1[1] % 20 == 0 and y_1[1] != 0:
            list_b.append(y_1[1])
    eliminate = []
    n = 1
    for xx in range(0, 39):
        k = 20 * n
        if list_b.count(k) >= 30:
            eliminate.append(k)
        n += 1
    return eliminate


# 判断下落的方块是否到底部
def numbers_t_or_f(argument, tetris):
    switcher = {
        1: (tetris[0])[1] < 780,
        2: (tetris[0])[1] < 780 and (tetris[1])[1] < 780,
        3: (tetris[0])[1] < 780 and (tetris[1])[1] < 780 and (tetris[2])[1] < 780,
        4: (tetris[0])[1] < 780 and (tetris[1])[1] < 780 and (tetris[2])[1] < 780 and (tetris[3])[1] < 780
    }
    return switcher.get(argument, "nothing")


# 游戏结束判断
def gameover(screen):
    time.sleep(1)
    font = pygame.font.Font(None, 60)  # 游戏结束显示
    text = font.render("Game Over", True, black)
    screen.fill(white)
    screen.blit(text, (210, 320))
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    sys.exit()


# 游戏循环
def ganmestart():
    # 进行游戏初始化
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((600, 800), 0, 0)
    pygame.display.set_caption("My PyGame")
    # 从左下开始构造，列出方块的各种形状和位置,共5种
    list = [[[280, -20], [300, -20], [280, -40], [280, -60]],  # 1
            [[280, -20], [280, -40], [280, -60], [280, -80]],  # 2
            [[280, -20], [300, -20], [320, -20], [300, -40]],  # 3
            [[280, -20], [300, -20], [280, -40], [300, -40]],  # 4
            [[280, -20], [300, -20], [300, -40], [320, -40]]]  # 5
    exist = 0
    FixedBlock = []
    change = 0
    # 游戏主循环
    while True:
        clock.tick(7)  # 控制下落速度
        direction = ""  # 初始化键盘接受的值
        # 判断从键盘接受的值
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 判断键盘事件
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "w"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "s"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "a"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "d"
                elif event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 如果当前下落方块为空，则随机生成一种方块
        if exist % 2 == 0:
            tetris = random.choice(list)  # 随机一个方块
            if tetris == [[280, -20], [300, -20], [280, -40], [280, -60]]:
                color = red
            if tetris == [[280, -20], [280, -40], [280, -60], [280, -80]]:
                color = blue
            if tetris == [[280, -20], [300, -20], [320, -20], [300, -40]]:
                color = purple
            if tetris == [[280, -20], [300, -20], [280, -40], [300, -40]]:
                color = yellow
            if tetris == [[280, -20], [300, -20], [300, -40], [320, -40]]:
                color = green
            exist += 1

            list = [[[280, -20], [300, -20], [280, -40], [280, -60]],  # 1
                    [[280, -20], [280, -40], [280, -60], [280, -80]],  # 2
                    [[280, -20], [300, -20], [320, -20], [300, -40]],  # 3
                    [[280, -20], [300, -20], [280, -40], [300, -40]],  # 4
                    [[280, -20], [300, -20], [300, -40], [320, -40]]]  # 5

        equal = ""  # 初始化方块是否重叠的值
        # 判断4个方块的坐标是否等于已下落完毕的方块的坐标，如果不是，则继续下落
        if (tetris[0])[1] < 780 and (tetris[1])[1] < 780 and (tetris[2])[1] < 780 and (tetris[3])[1] < 780:
            (tetris[0])[1] += 20
            (tetris[1])[1] += 20
            (tetris[2])[1] += 20
            (tetris[3])[1] += 20
            # 判断继续下落的方块是否重叠，如果重叠，则减少
            if exist > 1:
                equal = algorithm(tetris=tetris, FixedBlock=FixedBlock, equal="")
                if equal == "equal":
                    (tetris[0])[1] -= 20
                    (tetris[1])[1] -= 20
                    (tetris[2])[1] -= 20
                    (tetris[3])[1] -= 20
        # 若果下落到底，则把当前方块放入已下落完毕的方块数列中
        if (tetris[0])[1] >= 780 or (tetris[1])[1] >= 780 or (tetris[2])[1] >= 780 or (tetris[3])[
            1] >= 780 or equal == "equal":
            exist += 1
            tetris.append(color)
            FixedBlock.insert(0, tetris)
            # 如果一排时，进行消除
            num = eliminate(FixedBlock=FixedBlock)
            delete_2 = []
            change = 0
            if len(num) > 0:
                for delete_1 in FixedBlock:
                    z = 0
                    for x_1 in range(0, len(num)):
                        i = 0
                        for x_2 in range(0, len(delete_1)):
                            if (delete_1[i])[1] == num[z]:
                                if (delete_1[i])[0] % 20 == 0:
                                    delete_2.append((delete_1[i])[0])
                                delete_1.pop(i)

                                if i > len(delete_1) - 1:
                                    break
                            else:
                                if i < len(delete_1) - 1:
                                    i += 1
                                else:
                                    break
                        if z < len(num) - 1:
                            z += 1
                    if len(delete_1) == 1:
                        delete_1.pop(0)

                lens = len(num) - 1
                for delete_3 in FixedBlock:
                    for delete_4 in delete_3:
                        i = 0
                        if len(delete_4) > 0:
                            if delete_4[1] % 20 == 0 and delete_4[1] != 0:
                                if delete_4[1] <= num[i]:
                                    delete_4[1] += 20
                                if i < lens:
                                    i += 1
                        else:
                            delete_3.remove(delete_4)

        # 如果不重叠，则判断是否进行位移
        else:
            if numbers_t_or_f(len(tetris), tetris=tetris) == True:
                #  改变形状
                # 1顺时针改变
                # 2用颜色区别形状，在初始化变形的次数确定变形方位
                if direction == "w":
                    back_tetris = copy.deepcopy(tetris)
                    if color == purple:
                        if change == 0:
                            (tetris[0])[0] += 20
                            (tetris[0])[1] -= 20
                            (tetris[2])[0] -= 20
                            (tetris[2])[1] += 20
                            (tetris[3])[0] += 20
                            (tetris[3])[1] += 20
                            change += 1
                        elif change == 1:
                            (tetris[0])[0] += 20
                            (tetris[0])[1] += 20
                            (tetris[2])[0] -= 20
                            (tetris[2])[1] -= 20
                            (tetris[3])[0] -= 20
                            (tetris[3])[1] += 20
                            change += 1
                        elif change == 2:
                            (tetris[0])[0] -= 20
                            (tetris[0])[1] += 20
                            (tetris[2])[0] += 20
                            (tetris[2])[1] -= 20
                            (tetris[3])[0] -= 20
                            (tetris[3])[1] -= 20
                            change += 1
                        elif change == 3:
                            (tetris[0])[0] -= 20
                            (tetris[0])[1] -= 20
                            (tetris[2])[0] += 20
                            (tetris[2])[1] += 20
                            (tetris[3])[0] += 20
                            (tetris[3])[1] -= 20
                            change = 0
                    elif color == green:
                        if change == 0:
                            (tetris[0])[0] += 20
                            (tetris[0])[1] -= 20
                            (tetris[2])[0] += 20
                            (tetris[2])[1] += 20
                            (tetris[3])[1] += 40
                            change += 1
                        elif change == 1:
                            (tetris[0])[0] -= 20
                            (tetris[0])[1] += 20
                            (tetris[2])[0] -= 20
                            (tetris[2])[1] -= 20
                            (tetris[3])[1] -= 40
                            change = 0
                    elif color == red:
                        if change == 0:
                            (tetris[0])[1] -= 40
                            (tetris[1])[0] -= 20
                            (tetris[1])[1] -= 20
                            (tetris[2])[0] += 20
                            (tetris[2])[1] -= 20
                            (tetris[3])[0] += 40
                            change += 1
                        elif change == 1:
                            (tetris[0])[0] += 20
                            (tetris[1])[1] -= 20
                            (tetris[2])[1] += 20
                            (tetris[3])[0] -= 20
                            (tetris[3])[1] += 40
                            change += 1
                        elif change == 2:
                            (tetris[0])[0] += 20
                            (tetris[0])[1] += 20
                            (tetris[1])[0] += 40
                            (tetris[3])[0] -= 20
                            (tetris[3])[1] -= 20
                            change += 1
                        elif change == 3:
                            (tetris[0])[0] -= 40
                            (tetris[0])[1] += 20
                            (tetris[1])[0] -= 20
                            (tetris[1])[1] += 40
                            (tetris[2])[0] -= 20
                            (tetris[3])[1] -= 20
                            change = 0
                    elif color == blue:
                        if change == 0:
                            (tetris[0])[0] -= 20
                            (tetris[0])[1] -= 40
                            (tetris[1])[1] -= 20
                            (tetris[2])[0] += 20
                            (tetris[3])[0] += 40
                            (tetris[3])[1] += 20
                            change += 1
                        elif change == 1:
                            (tetris[0])[0] += 20
                            (tetris[0])[1] += 40
                            (tetris[1])[1] += 20
                            (tetris[2])[0] -= 20
                            (tetris[3])[0] -= 40
                            (tetris[3])[1] -= 20
                            change = 0
                    if exist > 1:
                        equal = algorithm(tetris=tetris, FixedBlock=FixedBlock, equal="")
                        if equal == "equal" or (tetris[0])[0] >= 580 or (tetris[1])[0] >= 580 or (tetris[2])[
                            0] >= 580 or (tetris[3])[
                            0] >= 580 or (tetris[0])[0] < 0 or (tetris[1])[0] < 0 or (tetris[2])[0] < 0 or (tetris[3])[
                            0] < 0:
                            tetris = back_tetris


                # 判断从键盘接受的数值进行增加
                elif direction == "s":
                    i = 0
                    for tetris_s in range(0, len(tetris)):
                        (tetris[i])[1] += 20
                        i += 1
                    # 如果重叠则减少
                    if equal != (algorithm(tetris=tetris, FixedBlock=FixedBlock, equal="")):
                        i = 0
                        for tetris_s_1 in range(0, len(tetris)):
                            (tetris[i])[1] -= 20
                            i += 1
                elif direction == "a" and (tetris[0])[0] > 0 and (tetris[1])[0] > 0 and (tetris[2])[0] > 0 and \
                        (tetris[3])[0] > 0:
                    i = 0
                    for tetris_a in range(0, len(tetris)):
                        (tetris[i])[0] -= 20
                        i += 1
                    if equal != (algorithm(tetris=tetris, FixedBlock=FixedBlock, equal="")):
                        i = 0
                        for tetris_a_1 in range(0, len(tetris)):
                            (tetris[i])[0] += 20
                            i += 1
                elif direction == "d" and (tetris[0])[0] < 580 and (tetris[1])[0] < 580 and (tetris[2])[0] < 580 and \
                        (tetris[3])[0] < 580:
                    i = 0
                    for tetris_d in range(0, len(tetris)):
                        (tetris[i])[0] += 20
                        i += 1
                    if equal != (algorithm(tetris=tetris, FixedBlock=FixedBlock, equal="")):
                        i = 0
                        for tetris_d in range(0, len(tetris)):
                            (tetris[i])[0] -= 20
                            i += 1
        # 填充背景
        screen.fill(black)
        # 正在下落方块的绘画
        for number in tetris:
            # 判断当前坐标是否为颜色的值，如果不是，则进行绘画
            if number != green and number != blue and number != yellow and number != red and number != purple:
                pygame.draw.rect(screen, color, Rect(number[0], number[1], 20, 20))
        # 已到底或重叠方块的绘画
        for undergrounds in FixedBlock:
            # 将当前方块的颜色存在color_1中
            if len(undergrounds) > 1:
                color_1 = undergrounds[len(undergrounds) - 1]
                for underground in undergrounds:
                    # 判断当前坐标是否为颜色的值，如果不是，则进行绘画
                    if underground != green and underground != blue and underground != yellow and underground != red and underground != purple:
                        pygame.draw.rect(screen, color_1, Rect(underground[0], underground[1], 20, 20))
                        # 如果y轴的值为0，则游戏结束
                        if underground[1] == 0:
                            gameover(screen)

        # 更新显示
        pygame.display.flip()


if __name__ == '__main__':
    # pygame.display.set_mode(size=(400, 400), flags=0, depth=0)
    purple = (255, 0, 255)
    green = 50, 205, 50
    blue = 123, 104, 238
    yellow = 238, 179, 34
    red = 255, 0, 0
    white = 255, 255, 255
    black = 0, 0, 0
    ganmestart()