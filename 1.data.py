import math as mth
from random import random as rd, choice as ch

s = "Hello World"

num = 1997.0

s = r"hello \'Yann.\'; \nname: YXD"  # str[0] = "h" 不允许修改
# print('Yann' in s) # 输出True
# print('Yannd' in s) # 输出False
# print(s[:]) # 输出字符串
# print(s[:5]) # 输出字符串前5个字符
# print(s[::-1]) # 输出字符串倒序
# print(s[::2]) # 输出字符串，间隔为2
# print(s[0:-1:2] * 2) # 输出从第一个开始到倒数第二个字符，且间隔为2；输出两次
# print(type(s))
# print(isinstance(s, str))
# print(s.upper())
# print(len(s))
s = "hello\\world\
!\
no, is py."
tp = ("Yann", 25, "Male")
s = "hello %s, i'm %d, is %s" % tp
s = """
hello
python
i'm a (\t).
"""
s = "hello %s" % "Yann"
s = f"format {1+2=} => {s}"
# print(s)

num += mth.pi
# print(rd(), ch(range(90, 100)))  # 输出一个随机数，一个90-100的随机数
# print("float:", num / 10, "int:", num // 10)


"""
inputNum = int(input("请输入数字："))
print("输出的数字：", inputNum, end=" ==> ")

if inputNum == 1997:
    print("输入的数字是1997")
else:
    print("输入的数字不是1997")
"""

for i in range(3, 7, 2):  # 间隔2个
    # print(i) # 输出 3 5
    continue

x, y = 1, 1

x, y = y, x + 2

# print(x, y) # 输出 1 3

while True:
    x += 1
    # print("hello world")
    if x == y:
        break


class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

# print(isinstance(dog, Animal))
# print(type(dog) == Dog)
# print(type(dog) == Animal)

# print(True + True)
# print(True and False, True & False)
# print(False or True, False | True)
