mylist = list(range(1,10,1))
mytuple=tuple(range(1,10,1))
myset=set(range(1,10,1))
print(mylist)
print(mytuple)
print(myset)


# import this







# # 自定义异常类，继承Exception
# class ShortInputError(Exception):
#     def __init__(self, length, min_len):
#         self.length = length
#         self.min_len = min_len

#     # 设置抛出异常的描述信息
#     def __str__(self):
#         return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'


# def main():
#     try:
#         con = input('请输入密码：')
#         if len(con) < 3:
#             raise ShortInputError(len(con), 3)
#     except Exception as result:
#         print(result)
#     else:
#         print('密码已经输入完成')


# main()





# #  1.我们要区分是水果，需要有一个水果类型
# #  2. 颜色和价格是对象属性
# #  3. 魔法方法__str__ 便于格式化打印对象
# class Fruit():
#     def __init__(self, fruit_type):
#         # 创建的时候指定创建什么类型的水果
#         self.type = fruit_type
#         self.color = None
#         self.price = None
#     # 设置颜色   
#     def Set_color(self,color):
#         self.color = color
#     # 设置价格
#     def Set_price(self,price):
#         self.price = price
        
#     def __str__(self):
#         if self.color is None or  self.price is None:
#             return "水果价格和颜色没有设置!"
#        	else:
#             return f'{self.type}: color--{self.color} price--{self.price}元 '

# # 创建苹果
# apple = Fruit("苹果")
# # apple.Set_color('red')
# # apple.Set_price(5)
# print(apple)

# .... 其他自己创建




# # src: 原始字符串，dst: 要查找的字符串
# def findall(src,dst):
#     # 获取字符长度，用去截取字符
#     lg = len(dst)
#     # 保存查找的下标
#     res = []
#     #遍历字符通过下标
#     for index in range(len(src)):
#         # 截取与dst相同的字符如果相等说明 位置ok
#         if src[index:index+lg]==dst:
#             # 把当前位置添加到结果集中
#             res.append(index)
            
#     # 把结果转化成元组返回       
#     return tuple(res)

# s = "helloworldhellopythonhelloc++hellojava"
# print(findall(s,"hello"))





# def findall(src,dst):
#     # 获取字符长度，用去截取字符
#     lg = len(dst)
#     print(lg)
#     # 保存查找的下标
#     res = []
#     #遍历字符通过下标
#     for index in range(len(src)):
#         # 截取与dst相同的字符如果相等说明 位置ok
#         # print(index)
#         if src[index:index+lg]==dst:
#             # 把当前位置添加到结果集中
#             res.append(index)
            
#     # 把结果转化成元组返回       
#     return tuple(res)

# s = "ababaababa"
# # s = "helloworldhellopythonhelloc++hellojava"
# # findall(s,'ab')
# print(findall(s,'aba'))


# # 1. 因为要处理每个字符，所以需要遍历字符
# # 2. 如果判断一个字符是不是英文字母，我们字符串本身就有方法可以判断 isalpha 方法
# # 3. 把英文单词拼接到一起就是我们要的
# msg = "hel@#$lo pyt \nhon ni\t hao%$" 
# # 保存结果
# result = ""
# # 循环遍历字符
# for s in msg:
#     # 判断当前字符是否是字母
#     if s.isalpha():
#         # 把字符添加到结果中
#         result+=s
# # 打印最后的结果      
# print(result)




# # 考察元组遍历，列表元素添加，列表元素判断，元组元素统计

# test = ("a", "b", "c", "a", "c")

# # 定义列表用于存储统计结果
# result = []

# for s in test:
#     cnt = test.count(s)
#     tmp = (s,cnt)
#     if tmp in result:
#         continue
#     else:
#         result.append(tmp)


# # 打印统计结果 
# print(result)





# a = "abcd"
# # 方法一 使用while逆向遍历
# # 获取字符串最大的下标
# index = len(a)-1
# while index>=0:
#     print(a[index],end='')
#     # 下标递减
#     index-=1

# print()
# # 方法二使用切片
# a = a[::-1]
# print(a)




# # 星号先递增值5个，然后再递减至5个
# # 可以考虑使用一个标志来控制星号的增加加和减少
# # 字符串可以使用乘法 '*'*5 表示 星号重复5次


# #初始要打印的星号个数
# num = 1
# # 设置一个标志，如果true 表示要星号增加
# flag = True

# # 星号小于0的时候退出循环
# while num>0:
#     # 打印星星
#     print("*"*num)
#     # 如果星号已经到5，更改flag,下次循环要开始减少星星
#     if num==5:
#         flag = False
        
#     # 如果flag 为true 说明星号是递增，
#     if flag:
#         num+=1
     
#     # flag为false 说明星号开始递减
#     else:
#         num-=1





# int = 100
# print(int)
# a = "200"
# b = int(a)
# print(b)




# # 刚开始会基本使用print即可
# print("==========我的名片==========")
# print("姓名: itheima")
# print("QQ:xxxxxxx")
# print("手机号:185xxxxxx")
# print("公司地址:北京市xxxx")
# print("===========================")




# class A(object):
#     a = 0

#     def __init__(self):
#         self.b = 1


# aa = A()
# # 返回类内部所有属性和方法对应的字典
# print(A.__dict__)
# # 返回实例属性和值组成的字典
# print(aa.__dict__)



# try:
#     print(1/1)
# except:
#     print(0/1)
# else:
#     print("完成")



# import os

# for i in range(0,1000):
#     print(i,end=' ')

# os.system("clear")













# class cal:
#     cal_name = '计算器'

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @property  # 在cal_add函数前加上@property，使得该函数可直接调用，封装起来
#     def cal_add(self):
#         return self.x + self.y

#     @classmethod  # 在cal_info函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性
#     def cal_info(cls):  # python自动传入位置参数cls就是类本身
#         print('这是一个%s' % cls.cal_name)  # cls.cal_name调用类自己的数据属性

#     @staticmethod  # 静态方法 类或实例均可调用
#     def cal_test(a, b, c):  # 改静态方法函数里不传入self 或 cls
#         print(a, b, c)


# c1 = cal(10,11)
# cal.cal_test(1,2,3)     #>>> 1 2 3
# c1.cal_test(1,2,3)      #>>> 1 2 3
# # cal.cal_info()
# # c1.cal_info()





# class A(object):
#     a = 0

#     def __init__(self):
#         self.b = 1


# aa = A()
# # 返回类内部所有属性和方法对应的字典
# print(A.__dict__)
# # 返回实例属性和值组成的字典
# print(aa.__dict__)


# class ShortInputError(Exception):
#     def __init__(self, length, min_len):
#         self.length = length
#         self.min_len = min_len

#     # 设置抛出异常的描述信息
#     def __str__(self):
#         return f'你输入的长度是{self.length}, 不能少于{self.min_len}个字符'


# def main():
#     try:
#         con = input('请输入密码：')
#         if len(con) < 10:
#             raise ShortInputError(len(con), 10)
#     except Exception as result:
#         print(result)
#     else:
#         print('密码已经输入完成')

#     finally:
#         print("完成步骤！")

# main()


# # print(type(str(1)))
# # print(type(1))


# import time

# # f = open('test.txt','w')

# # for i in range(0,10000000):
# #     f.write(str(i)+' ')
# # f.close()

# try:
#     f = open('test01.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             # time.sleep(2)
#             print(content)
#     except:
#         # 如果在读取文件的过程中，产生了异常，那么就会捕获到
#         # 比如 按下了 ctrl+c
#         print('意外终止了读取数据')
#     finally:
#         f.close()
#         print('关闭文件')
# except:
#     print("没有这个文件")


# try:
#     f = open('test.txt', 'r')
# except Exception as result:
#     print(result)
#     f = open('test.txt', 'w')
# else:
#     print('没有异常，真开心')
# finally:
#     f.close()


# try:
#     print(1)
# except Exception as result:
#     print(result)
# else:
#     print('我是else，是没有异常的时候执行的代码')

# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as result:
#     print(result)

# try:
#     print(num)
# except NameError:
#     print('有错误')


# class Furniture():
#     def __init__(self, name, area):
#         # 家具名字
#         self.name = name
#         # 家具占地面积
#         self.area = area

# class Home():
#     def __init__(self, address, area):
#         # 地理位置
#         self.address = address
#         # 房屋面积
#         self.area = area
#         # 剩余面积
#         self.free_area = area
#         # 家具列表
#         self.furniture = ["地板"]

#     def __str__(self):
#         print(f'房子坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有',end=" ")
#         for i in self.furniture:
#                 print(i,end=' ')
#         return ' '


#     def add_furniture(self, item):
#         """容纳家具"""
#         if self.free_area >= item.area:
#             self.furniture.append(item.name)
#             # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积
#             self.free_area -= item.area
#         else:
#             print('家具太大，剩余面积不足，无法容纳')

# bed = Furniture('双人床', 6)
# jia1 = Home('北京', 1200)
# print(jia1)

# jia1.add_furniture(bed)
# print(jia1)

# sofa = Furniture('沙发', 10)
# jia1.add_furniture(sofa)
# print(jia1)

# ball = Furniture('篮球场', 1500)
# jia1.add_furniture(ball)
# print(jia1)


# class SweetPotato():
#     def __init__(self):
#         # 被烤的时间
#         self.cook_time = 0
#         # 地瓜的状态
#         self.cook_static = '生的'
#         # 调料列表
#         self.condiments = []

#     def cook(self, time):
#         """烤地瓜的方法"""
#         self.cook_time += time
#         if 0 <= self.cook_time < 3:
#             self.cook_static = '生的'
#         elif 3 <= self.cook_time < 5:
#             self.cook_static = '半生不熟'
#         elif 5 <= self.cook_time < 8:
#             self.cook_static = '熟了'
#         elif self.cook_time >= 8:
#             self.cook_static = '烤糊了'

#     def add_condiments(self, condiment):
#         """添加调料"""
#         self.condiments.append(condiment)

#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟, 状态是{self.cook_static}, 添加的调料有{self.condiments}'


# digua1 = SweetPotato()
# print(digua1)

# digua1.cook(2)
# digua1.add_condiments('酱油')
# print(digua1)

# digua1.cook(2)
# digua1.add_condiments('辣椒面儿')
# print(digua1)

# digua1.cook(2)
# print(digua1)

# digua1.cook(2)
# print(digua1)


# class SweetPotato():
#     def __init__(self):
#         # 被烤的时间
#         self.cook_time = 0
#         # 地瓜的状态
#         self.cook_static = '生的'
#         # 调料列表
#         self.condiments = []

#     def cook(self, time):
#         """烤地瓜的方法"""
#         self.cook_time += time
#         if 0 <= self.cook_time < 3:
#             self.cook_static = '生的'
#         elif 3 <= self.cook_time < 5:
#             self.cook_static = '半生不熟'
#         elif 5 <= self.cook_time < 8:
#             self.cook_static = '熟了'
#         elif self.cook_time >= 8:
#             self.cook_static = '烤糊了'

#     def add_condiments(self, condiment):
#         """添加调料"""
#         self.condiments.append(condiment)

#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟, \
#             状态是{self.cook_static}, 添加的调料有\
#                 {self.condiments}'


# digua1 = SweetPotato()
# print(digua1)

# digua1.cook(2)
# digua1.add_condiments('酱油')
# print(digua1)

# digua1.cook(2)
# digua1.add_condiments('辣椒面儿')
# print(digua1)

# digua1.cook(2)
# print(digua1)

# digua1.cook(2)
# print(digua1)


# class Washer():
#     def __init__(self, width, height, myname):
#         self.width = width
#         self.height = height
#         self.name = myname

#     def __del__(self):
#         print(f'{self.name}对象已经被删除')

#     def __str__(self):
#         return self.name


# haier1 = Washer(10, 20, "haier1")

# print(haier1)
# print(haier1.name)


# # print(haier1)

# # <__main__.Washer object at 0x0000026118223278>对象已经被删除
# del haier1


# class Washer():
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def print_info(self):
#         print(f'洗衣机的宽度是{self.width}')
#         print(f'洗衣机的高度是{self.height}')


# haier1 = Washer(10, 20)
# haier1.print_info()


# haier2 = Washer(30, 40)
# haier2.print_info()


# class Washer():

#     # 定义初始化功能的函数
#     def __init__(self):
#         # 添加实例属性
#         self.width = 500
#         self.height = 800


#     def print_info(self):
#         # 类里面调用实例属性
#         print(f'洗衣机的宽度是{self.width}, 高度是{self.height}')


# haier1 = Washer()
# haier1.print_info()


# class Washer():
#     def print_info(self):
#         # 类里面获取实例属性
#         print(f'haier1洗衣机的宽度是{self.width}')
#         print(f'haier1洗衣机的高度是{self.height}')

# # 创建对象
# haier1 = Washer()

# # 添加实例属性
# haier1.width = 500
# haier1.height = 800

# haier1.print_info()


# class Washer():
#     def wash(self):
#         print('我会洗衣服')
#         # <__main__.Washer object at 0x0000024BA2B34240>
#         print(self)


# # 2. 创建对象
# haier1 = Washer()
# # <__main__.Washer object at 0x0000018B7B224240>
# print(haier1)
# # haier1对象调用实例方法
# haier1.wash()


# haier2 = Washer()
# # <__main__.Washer object at 0x0000022005857EF0>
# print(haier2)

# haier2.wash()

# haier1.width = 500
# haier1.height = 800

# print(f'haier1洗衣机的宽度是{haier1.width}')
# print(f'haier1洗衣机的高度是{haier1.height}')


# import os

# new_name = input("请输入要创建的文件夹名：")
# new_file = input("请输入要创建的文件名：") + ".txt"

# # dir_name = os.getcwd() +"./"
# old_path = os.getcwd()  #获得当前目录

# index = old_path.rfind("\\") #获得上一级目录
# new_path = old_path[:index+1]

# # print(old_path)
# # print(new_path)

# os.mkdir(new_path+new_name) #在上一级目录添加文件夹

# new_dir = os.listdir(new_path)  #遍历目录，获得新添加的文件夹

# for name in new_dir:
#     if name == new_name:
#         myFilePath = new_path + new_name + '/'  #获得新添加文件中的路径
#         break

# f = open(myFilePath + new_file,'w')

# f.write("hello,world")

# f.close()


# now_p = os.listdir(dir_name)

# for name in now_p:
#     if name == new_name:
#         new_dir_name = dir_name + "/" + new_name + "/"
#         break

# new_name += ".txt"
# f = open(new_dir_name + new_name, 'w')

# f.write("hello,world!!!")

# f.close()

# import os

# new_name = input("请输入要创建的文件夹名：")

# # dir_name = os.getcwd() +"./"
# dir_name = os.getcwd()

# os.mkdir(new_name)

# now_p = os.listdir(dir_name)

# for name in now_p:
#     if name == new_name:
#         new_dir_name = dir_name + "/" + new_name + "/"
#         break

# new_name += ".txt"
# f = open(new_dir_name + new_name, 'w')

# f.write("hello,world!!!")

# f.close()


# import os

# # old_name = input("请输入想要更改的文件名：")
# # new_name = input("请输入新的文件名：")

# dir_name = os.getcwd() +"./"
# # dir_name = os.getcwd()

# now_p = os.listdir(dir_name)

# print(now_p)

# for name in now_p:
#     if name == old_name:
#         os.rename(dir_name+name, dir_name+new_name)
#         break


# import os

# # 设置重命名标识：如果为1则添加指定字符，flag取值为2则删除指定字符
# flag = 1

# # 获取指定目录
# dir_name = './'

# # 获取指定目录的文件列表
# file_list = os.listdir(dir_name)
# # print(file_list)


# # 遍历文件列表内的文件
# for name in file_list:

#     # 添加指定字符
#     if flag == 1:
#         new_name = 'Python-' + name
#     # 删除指定字符
#     elif flag == 2:
#         num = len('Python-')
#         new_name = name[num:]

#     # 打印新文件名，测试程序正确性
#     print(new_name)

#     # 重命名
#     os.rename(dir_name+name, dir_name+new_name)


# old_name = input('请输入您要备份的文件名：')

# index = old_name.rfind('.')


# while index <= 0:
#     print("error!!")
#     old_name = input('请输入您要备份的文件名：')
#     index = old_name.rfind('.')

# postfix = old_name[index:]
# new_name = old_name[:index] + '[备份]' + postfix

# old_f = open(old_name, 'rb')
# new_f = open(new_name, 'wb')

# while True:
#     con = old_f.read(1024)
#     if len(con) == 0:
#         break
#     new_f.write(con)

# old_f.close()
# new_f.close()


# old_name = input('请输入您要备份的文件名：')

# # 2.1 提取文件后缀点的下标
# index = old_name.rfind('.')

# print(index)  # 后缀中.的下标

# print(old_name[:index])  # 源文件名（无后缀）

# # 2.2 组织新文件名 旧文件名 + [备份] + 后缀
# new_name = old_name[:index] + '[备份]' + old_name[index:]

# # 打印新文件名（带后缀）
# print(new_name)

# # 3.1 打开文件
# old_f = open(old_name, 'rb')
# new_f = open(new_name, 'wb')

# # 3.2 将源文件数据写入备份文件
# while True:
#     con = old_f.read(1024)
#     if len(con) == 0:
#         break
#     new_f.write(con)

# # 3.3 关闭文件
# old_f.close()
# new_f.close()


# print("备份成功！")

# new_f=open(new_name,'r')

# print(new_f.read())


# # 1. 打开文件
# f = open('test.txt', 'w')

# # 2.文件写入
# f.write('hello world\n')

# f.close()

# f = open('test.txt','a')
# f.write('ytrhtrfh\n')
# f.write('faefe\n')

# f.close()


# # f = open('test.txt')
# # content = f.readlines()

# # # ['hello world\n', 'abcdefg\n', 'aaa\n', 'bbb\n', 'ccc']
# # print(content)

# # # 3. 关闭文件
# # f.close()

# f = open("test.txt", "r")

# f.seek(5,0)
# # f.seek(3,1)

# content01 = f.read()
# print(content01)

# # 3. 关闭文件
# f.close()


# list1 = [1, 2, 3, 4, 5]


# def func(x):
#     return x ** 2


# result = map(func, list1)

# print(result)  # <map object at 0x0000013769653198>
# print(list(result))  # [1, 4, 9, 16, 25]


# list1 = [1, 2, 3, 4, 5]


# def func(x):
#     return x ** 2


# result = map(func, list1)

# print(result)  # <map object at 0x0000013769653198>


# list01=list(result)
# print(list01)  # [1, 4, 9, 16, 25]

# for i in list01:
#     print(i)


# def sum_num(a, b, f):
#     return f(a) + f(b)


# result = sum_num(-1, 2, abs)
# print(result)  # 3

# result = sum_num(-1.1, 2.5, round)

# print(result)  # 3


# students = [
#     {'name': 'TOM', 'age': 20},
#     {'name': 'ROSE', 'age': 19},
#     {'name': 'Jack', 'age': 22}
# ]

# # 按name值升序排列
# students.sort(key=lambda x: x['name'])
# print(students)

# # 按name值降序排列
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)

# # 按age值升序排列
# students.sort(key=lambda x: x['age'])
# print(students)

# fn1 = lambda **kwargs: kwargs
# print(fn1(name='python', age=20))

# fn1 = lambda a, b, c=100: a + b + c
# print(fn1(10, 20))

# fn1 = lambda *args: args
# print(fn1(10, 20, 30))

# fn1 = lambda: 100
# print(fn1())


# fn1 = lambda a, b: a + b
# print(fn1(1, 2))


# def fn1():
#     return 200


# print(fn1)
# print(fn1())


# # lambda表达式
# fn2 = lambda: 100
# print(fn2)
# print(fn2())


# def sum_numbers(num):
#     # 1.如果是1，直接返回1 -- 出口
#     if num == 1:
#         return 1
#     # 2.如果不是1，重复执行累加并返回结果
#     return num + sum_numbers(num-1)


# sum_result = sum_numbers(3)
# # 输出结果为6
# print(sum_result)


# def print_info():
#     print('-' * 20)
#     print('欢迎登录学员管理系统')
#     print('1: 添加学员')
#     print('2: 删除学员')
#     print('3: 修改学员信息')
#     print('4: 查询学员信息')
#     print('5: 显示所有学员信息')
#     print('6: 退出系统')
#     print('-' * 20)

# #############################


# def add_info():
#     """ 添加学员 """
#     # 接收用户输入学员信息
#     new_id = input('请输入学号：')
#     new_name = input('请输入姓名：')
#     new_tel = input('请输入手机号：')

#     # 声明info是全局变量
#     global info

#     # 检测用户输入的姓名是否存在，存在则报错提示
#     for i in info:
#         if new_name == i['name']:
#             print('该用户已经存在！')
#             return

#     # 如果用户输入的姓名不存在，则添加该学员信息
#     info_dict = {}

#     # 将用户输入的数据追加到字典
#     info_dict['id'] = new_id
#     info_dict['name'] = new_name
#     info_dict['tel'] = new_tel

#     # 将这个学员的字典数据追加到列表
#     info.append(info_dict)

#     print(info)

# #############################


# def modify_info():
#     """修改函数"""
#     # 1. 用户输入要修改的学员的姓名
#     modify_name = input('请输入要修改的学员的姓名：')

#     global info
#     # 2. 判断学员是否存在：如果输入的姓名存在则修改手机号，否则报错提示
#     for i in info:
#         if modify_name == i['name']:
#             i['tel'] = input('请输入新的手机号：')
#             break
#     else:
#         print('该学员不存在')

#     print(info)

# #############################


# def del_info():
#     """删除学员"""
#     # 1. 用户输入要删除的学员的姓名
#     del_name = input('请输入要删除的学员的姓名：')

#     global info
#     # 2. 判断学员是否存在:如果输入的姓名存在则删除，否则报错提示
#     for i in info:
#         if del_name == i['name']:
#             info.remove(i)
#             break
#     else:
#         print('该学员不存在')

#     print(info)

# #############################


# def search_info():
#     """查询学员"""
#     # 1. 输入要查找的学员姓名：
#     search_name = input('请输入要查找的学员姓名：')

#     global info
#     # 2. 判断学员是否存在：如果输入的姓名存在则显示这位学员信息，否则报错提示
#     for i in info:
#         if search_name == i['name']:
#             print('查找到的学员信息如下：----------')
#             print(f"该学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}")
#             break
#     else:
#         print('该学员不存在')

# #############################


# def print_all():
#     """ 显示所有学员信息 """
#     print('学号\t姓名\t手机号')
#     for i in info:
#         print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

# #############################


# info = []
# while True:
#     # 1. 显示功能界面
#     print_info()

#     # 2. 用户选择功能
#     user_num = input('请选择您需要的功能序号：')

#     # 3. 根据用户选择，执行不同的功能
#     if user_num == '1':
#         # print('添加学员')
#         add_info()
#     elif user_num == '2':
#         # print('删除学员')
#         del_info()
#     elif user_num == '3':
#         # print('修改学员信息')
#         modify_info()
#     elif user_num == '4':
#         # print('查询学员信息')
#         search_info()
#     elif user_num == '5':
#         # print('显示所有学员信息')
#         print_all()
#     elif user_num == '6':
#         # print('退出系统')
#         exit_flag = input('确定要退出吗？yes or no')
#         if exit_flag == 'yes':
#             break
#     else:
#         print('输入错误，请重新输入!!!')


# def user_info(**kwargs):
#     print(kwargs)
#     return kwargs


# # {'name': 'TOM', 'age': 18, 'id': 110}
# kwarg = user_info(name='TOM', age=18, id=110)
# a, b, c = kwarg
# print(a)
# print(b)
# print(c)

# print()
# print()
# print()

# print(kwarg[a])
# print(kwarg[b])
# print(kwarg[c])


# def test1(a):
#     print(a)
#     print(id(a))

#     a += a

#     print(a)
#     print(id(a))


# # int：计算前后id值不同
# b = 100
# test1(b)

# # 列表：计算前后id值相同
# c = [11, 22]
# test1(c)


# # 2. 列表
# aa = [10, 20]
# bb = aa

# print(id(aa))  # 2325297783432
# print(id(bb))  # 2325297783432


# aa.append(30)
# del aa[1]
# print(bb)  # [10, 20, 30], 列表为可变类型

# print(id(aa))  # 2325297783432
# print(id(bb))  # 2325297783432


# # 1. int类型
# a = 1
# b = a

# print(b)  # 1

# print(id(a))  # 140708464157520
# print(id(b))  # 140708464157520

# a = 2
# print(b)  # 1,说明int类型为不可变类型

# print(id(a))  # 140708464157552，此时得到是的数据2的内存地址
# print(id(b))  # 140708464157520


# # a, b = 1, 2
# a=1
# b=2
# a, b = b, a
# print(a)  # 2
# print(b)  # 1


# def user_info(*args):
#     print(args)
# # ('TOM',)
# user_info('TOM')
# # ('TOM', 18)
# user_info('TOM', 18,"jfioweajf")


# def mysum(a,b):
#     """求和函数"""
#     return a+b

# print(mysum(1,3))
# help(mysum)


# list1 = []
# for i in range(1,3):
#     for j in range(3):
#         if i >= j:
#             list1.append((i,j))
# print(list1)


# list1 = [i for i in range(0, 10) if i % 2 == 0]
# list2 = [i for i in range(0, 10, 2)]
# print(list1)
# print(list2)

# # print("hello,world")
# # age = int(input("请输入你的年龄："))
# # if age >= 18:
# #     print(f"你已经{age}岁了，可以上网！")
# # else:
# #     print(f"你才{age}岁，不能上网！")
# # print("系统关闭！")

# str1 = "abc,def,ghi,jkl,abc"
# # str2 = str1.replace("abc", "cba", -1)
# # print(str1)
# # print(str2)

# # list1 = ['a', 'b', 'c']
# # str3 = "0"
# # str4 = str3.join(list1)
# # print(str4)

# mylist = [1, 2, 3, 7, 4]
# # mylist.sort(reverse=False)

# mylist01=mylist
# mylist02=mylist01.copy()

# print(mylist01)
# print(mylist02)

# # print("mylist is %d,%d,%d,%d" % (mylist[0], mylist[1], mylist[2], mylist[3]))
# # print(f"mylist is {mylist[0]},{mylist[1]},{mylist[2]},{mylist[3]}")
