import pygame


# import pygame
# from pygame.locals import *
# from sys import exit
# SCREEN_SIZE = (640, 480)
# pygame.init()
# background_image_filename = r"E:\python_program\python_program\my_alien_invasion03\images\aliens\alien2.png"
# screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
# screen.fill((255,255,0))
# background = pygame.image.load(background_image_filename)
# while True:
#     screen.fill((255,255,0))
#     event = pygame.event.wait()
#     if event.type == QUIT:
#         exit()
#     if event.type == VIDEORESIZE:
#         # get the size of the window
#         SCREEN_SIZE = event.size
#         # set the mode of the window
#         screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
#         pygame.display.set_caption("Window resized to "+str(event.size))
#     screen_width, screen_height = SCREEN_SIZE
#     # change the background size
#     for y in range(0, screen_height, background.get_height()):
#         for x in range(0, screen_width, background.get_width()):
#             screen.blit(background, (x, y))




# import pygame
# import sys
# import random
# import math

# pygame.init()

# SIZE = WIDTH, HEIGHT = 800, 500
# BACKGROUND_COLOR = (230, 255, 230)

# screen = pygame.display.set_mode(SIZE)
# leaves = []


# class Leaf(object):
#     def __init__(self, pos=[10, 10], speed=[1, 1]):
#         self.imageSrc = pygame.image.load(r"E:\python_program\python_program\my_alien_invasion03\images\aliens\alien2.png")
#         self.rect = self.imageSrc.get_rect()
#         self.image = self.imageSrc
#         self.speed = speed
#         self.angle = 0
#         self.pos = pos
#         self.rect = self.rect.move(pos[0], pos[1])

#     def move(self):
#         self.rect = self.rect.move(self.speed[0], self.speed[1])
#         new_rect = self.image.get_rect()
#         new_rect.left, new_rect.top = self.rect.left, self.rect.top
#         if new_rect.left < 0 or new_rect.right > WIDTH:
#             self.speed[0] = -self.speed[0]
#             if new_rect.right > WIDTH:
#                 self.rect.left = WIDTH - new_rect.width
#             if new_rect.left < 0:
#                 self.rect.left = 0
#         if new_rect.top > HEIGHT:
#             self.rect.bottom = 0

#     def draw(self):
#         screen.blit(self.image, self.rect)

#     def rotate(self):
#         self.image = pygame.transform.rotate(self.imageSrc, self.angle)
#         # self.angle += random.randint(1, 5)
#         self.angle += 3
#         if math.fabs(self.angle) == 360:
#             self.angle = 0


# def init():
#     for i in range(0, 5):
#         leaf = Leaf([random.randint(50, WIDTH - 50), random.randint(30, HEIGHT)],
#                     [random.randint(1, 2), random.randint(1, 2)])
#         leaf.move()
#         leaves.append(leaf)


# clock = pygame.time.Clock()
# init()

# while True:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()

#     screen.fill(BACKGROUND_COLOR)

#     # 将旋转后的图象，渲染到新矩形里
#     for item in leaves:
#         item.rotate()
#         item.move()
#         item.draw()

#     # 正式渲染
#     pygame.display.update()
#     # 控制帧数<=100
#     clock.tick(200)





# import pygame
# import sys

# pygame.init()

# SIZE = WIDTH, HEIGHT = 200, 400
# BLACK = 0, 0, 0
# angle = 1

# screen = pygame.display.set_mode(SIZE)
# leaf = pygame.image.load(r"E:\python_program\python_program\my_alien_invasion03\images\aliens\alien2.png")
# leafRect = leaf.get_rect()
# leafRect = leafRect.move((WIDTH - leafRect.width) / 2,
#                           (HEIGHT - leafRect.height) / 2)

# clock = pygame.time.Clock()
# while True:

#     for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#             sys.exit()
#     keys = pygame.key.get_pressed()
#     # 旋转图片(注意：这里要搞一个新变量，存储旋转后的图片）
#     newLeaf = pygame.transform.rotate(leaf, angle)
#     # newLeaf = pygame.transform.smoothscale(newLeaf,(100,200))
#     # 校正旋转图片的中心点
#     newRect = newLeaf.get_rect(center=leafRect.center)
#     angle += 1
#     screen.fill(BLACK)
#     # 这里要用newRect区域，绘制图象
#     screen.blit(newLeaf, newRect)
#     pygame.draw.rect(screen, (255, 0, 0), leafRect, 1)
#     pygame.draw.rect(screen, (0, 255, 0), newRect, 1)
#     pygame.display.update()
#     clock.tick(100)

# import pygame
# import sys

# pygame.init()

# SIZE = WIDTH, HEIGHT = 500, 400
# BLACK = 0, 0, 0
# angle = 1

# screen = pygame.display.set_mode(SIZE)
# leaf = pygame.image.load(r"E:\python_program\python_program\my_alien_invasion03\images\aliens\alien2.png")
# leafRect = leaf.get_rect()
# leafRect = leafRect.move((WIDTH - leafRect.width) / 2,
#                           (HEIGHT - leafRect.height) / 2)

# clock = pygame.time.Clock()
# while True:
#     for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              sys.exit()
#     keys = pygame.key.get_pressed()
#     # 旋转图片(注意：这里要搞一个新变量，存储旋转后的图片）
#     newLeaf = pygame.transform.rotate(leaf, angle)
#     newRect = newLeaf.get_rect()
#     angle += 1
#     screen.fill(BLACK)
#     screen.blit(newLeaf, leafRect)
#     pygame.draw.rect(screen, (255, 0, 0), leafRect, 1)
#     pygame.draw.rect(screen, (0, 255, 0), newRect, 1)
#     pygame.display.update()
#     clock.tick(100)

# import os
# if if __name__ == "__main__":
#     print("你好")
#     os.system("pause")


# import os

# filepath = os.getcwd()

# print("输出为：" + filepath)


# from tkinter import *
# import time
# import threading


# import tkinter as tk  # 使用Tkinter前需要先导入

# # 第1步，实例化object，建立窗口window
# window = tk.Tk()


# # 第2步，给窗口的可视化起名字
# window.title('Help documentation')

# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300+500+100')  # 这里的乘是小x

# window.resizable(0,0) #防止用户调整尺寸


# filename = r"E:\python_program\python_program\my_alien_invasion02\help_document.txt"
# f_open = open(filename)
# content = f_open.read()
# f_open.close()
# # 第4步，在图形界面上设定标签
# l = tk.Label(window, text=content, bg="lightgreen", justify=LEFT,
#              font=('Arial', 12), width=30, height=10)
# # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高


# # 第5步，放置标签
# # l.place(rely=1, relx=0.5, x=-150, y=-150)    # Label内容content区域放置位置，自动调节尺寸
# l.pack()
# # 放置lable的方法有：1）l.pack(); 2)l.place();

# m = tk.Label(window,fg = "red" ,anchor='w')
# m.place(relx = 0.5,rely = 0.8,anchor = CENTER)

# def autoClose():
#     for i in range(10):
#         m["text"] = "距离窗口关闭还有{}秒".format(10-i)
#         time.sleep(1)
#     window.destroy()

# t = threading.Thread(target=autoClose)
# t.start()


# # 第6步，主窗口循环显示
# window.mainloop()
# # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
# # 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，
# # mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，
# # 所以我们必须要有循环
