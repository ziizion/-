import math
from asyncore import write


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b
def sqrt(a):
    if a <0:
        raise ValueError("负数不能开方")
    return math.sqrt(a)

def memory(content):
    with open("memory.txt","a",encoding="utf-8") as f:
        f.write(content+"\n")

def read():
    try:
        with open("memory.txt","r",encoding="utf-8") as f:
            lines=f.readlines()
        if not lines:
            print("无记录")
            return
        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print("不存在文件")

while True:
    print("""
    0、退出    1、加法    2、减法    3、乘法    4、除法    5、幂运算   
    6、开方    7、查看历史记录""")
    try:
        a=int(input("输入数字进行选择"))
        if a==0:
            print("欢迎下次使用")
            break
        elif a in (1,2,3,4,5):
            a1=float(input("请输入第一个数字"))
            a2=float(input("请输入第二个数字"))
            b1=None
            b2=""
            if a ==1:
                b1=add(a1,a2)
                b2=f"{a1}+{a2}={b1}"
            elif a==2:
                b1=sub(a1,a2)
                b2=f"{a1}-{a2}={b1}"
            elif a==3:
                b1=mul(a1,a2)
                b2=f"{a1}*{a2}={b1}"
            elif a==4:
                b1=div(a1,a2)
                b2=f"{a1}/{a2}={b1}"
            elif a==5:
                b1=pow(a1,a2)
                b2=f"{a1}**{a2}={b1}"
            print("计算结果：",b2)
            memory(b2)
        elif a == 6:
            a3=float(input("输入需要开方的数字"))
            b1=sqrt(a3)
            b2=f"√{a3}={b1}"
            print("计算结果：", b2)
            memory(b2)
        elif a == 7:
            read()
        else:
            print(" 无效输入")
    except ValueError as e:
        print(f"错误：{e}，")
    except ZeroDivisionError as e:
        print(f"错误：{e}")
    except Exception as e:
        print(f"错误：{e}")


