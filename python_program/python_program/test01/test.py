from max import max
import os

if __name__ == '__main__':
    a=1
    b=-1
    print(max(a,b))

    try:
        # f_path = os.getcwd() + r"\my_txt.txt"
        f = open(r"E:\python_program\python_program\test01\my_txt.txt")
        print(f.read())
        f.close()
    except Exception:
        os.system("pause")

    os.system("pause")

    