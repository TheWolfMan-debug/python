import os

new_name = input("请输入要创建的文件夹名：")

# dir_name = os.getcwd() +"./"
dir_name = os.getcwd()

os.mkdir(new_name)

now_p = os.listdir(dir_name)

for name in now_p:
    if name == new_name:
        new_dir_name = dir_name + "/" + new_name + "/"
        break

new_name += ".txt"
f = open(new_dir_name + new_name, 'w')

f.write("hello,world!!!")

f.close()