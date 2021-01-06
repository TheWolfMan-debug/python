import os

new_name = input("请输入要创建的文件夹名：")
new_file = input("请输入要创建的文件名：") + ".txt"

# dir_name = os.getcwd() +"./"
old_path = os.getcwd()  #获得当前目录

index = old_path.rfind("\\") #获得上一级目录
new_path = old_path[:index+1]

# print(old_path)
# print(new_path)

os.mkdir(new_path+new_name) #在上一级目录添加文件夹

new_dir = os.listdir(new_path)  #遍历目录，获得新添加的文件夹

for name in new_dir:
    if name == new_name:
        myFilePath = new_path + new_name + '/'  #获得新添加文件中的路径
        break

f = open(myFilePath + new_file,'w')

f.write("hello,world")

f.close()
