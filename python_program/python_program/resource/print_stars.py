# 星号先递增值5个，然后再递减至5个
# 可以考虑使用一个标志来控制星号的增加加和减少
# 字符串可以使用乘法 '*'*5 表示 星号重复5次


#初始要打印的星号个数
num = 1
# 设置一个标志，如果true 表示要星号增加
flag = True

# 星号小于0的时候退出循环
while num>0:
    # 打印星星
    print("*"*num)
    # 如果星号已经到5，更改flag,下次循环要开始减少星星
    if num==5:
        flag = False
        
    # 如果flag 为true 说明星号是递增，
    if flag:
        num+=1
     
    # flag为false 说明星号开始递减
    else:
        num-=1