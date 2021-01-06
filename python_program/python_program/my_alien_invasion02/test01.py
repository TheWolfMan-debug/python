from tkinter import *
import time
import threading


import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()


# 第2步，给窗口的可视化起名字
window.title('Help documentation')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300+500+100')  # 这里的乘是小x

window.resizable(0,0) #防止用户调整尺寸


filename = r"E:\python_program\python_program\my_alien_invasion02\help_document.txt"
f_open = open(filename)
content = f_open.read()
f_open.close()
# 第4步，在图形界面上设定标签
l = tk.Label(window, text=content, bg="lightgreen", justify=LEFT,
             font=('Arial', 12), width=30, height=10)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高


# 第5步，放置标签
# l.place(rely=1, relx=0.5, x=-150, y=-150)    # Label内容content区域放置位置，自动调节尺寸
l.pack()
# 放置lable的方法有：1）l.pack(); 2)l.place();

m = tk.Label(window,fg = "red" ,anchor='w')
m.place(relx = 0.5,rely = 0.8,anchor = CENTER)

def autoClose():
    for i in range(10):
        m["text"] = "距离窗口关闭还有{}秒".format(10-i)
        time.sleep(1)
    window.destroy()

t = threading.Thread(target=autoClose)
t.start()



# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
# 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，
# mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，
# 所以我们必须要有循环


