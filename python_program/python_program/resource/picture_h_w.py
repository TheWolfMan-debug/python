def readInt(imgFile,offset):
    #把文件指针移动到文件中指定字节处。
    imgFile.seek(offset)
    #读取4个独立的字节并转换为整数
    theBytes = imgFile.read(4)
    result=0
    base = 1
    for i in range(4):
        print(theBytes[i],end=" ")
        result = result + theBytes[i]*base
        base = base * 256

    print(f"\n{result}")
    return result

def main():
    # filename = input("Please enter the file name:")
    filename = "test.bmp"

    #以可读可写的二进制文件模式打开。
    imgFile = open(filename,"rb")

    #提取图像信息。
    width = readInt(imgFile,18)
    height = readInt(imgFile,22)

    print("the width and height of the image is",width ,height)


main()