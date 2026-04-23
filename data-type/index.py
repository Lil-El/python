import math as mth

from random import random as rd, choice as ch, shuffle

s = "Hello World"

num = 1997.0

tp = (1, 2, 3, 4, 5)

arr = [1, 2, 3, 4, 5]
shuffle(arr)  # 随机排序

obj = {"name": "John", "age": 25}

st = {"10", "20", "30", "40", "50"}  # 无序不重复

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

tp = (2,)  # 元组只有一个元素时，必须加逗号
t1, t2 = tp + (1,), tp * 2
# print(t1, t2)
# tp[0] = 2 不允许修改
# print(tp[0:1], len(tp))

arr.append(6)
arr.remove(6)
arr.sort()  # 修改原列表，不返回新的列表
arr += [6] + [7, 8] * 2
arr[0:2] = [-2, -1]
del arr[0:2]
print(arr)
print(min(arr))
# print(sum(arr))

st.add(4)  # st + set(2) 不允许修改
# print("4 in st:", 4 in st)
st.discard("10")
# print('"10" not in st:', "10" not in st)
# for i in st:
#     print(i)

st = ()
# print(type(st)) # tuple
st = {}
# print(type(st)) # dict
st = set()
# print(type(st)) # set
st = set("hello")
# print(st) # set {'h', 'l', 'e', 'o'}

# 集合运算
# print(st & set("world"))
# print(st - set("world"))

# print(obj.keys(), obj["name"])
del obj["age"]
# print(obj)
lastKey = list(obj.keys())[0]
tpLastKey = tuple(obj.keys())[0]

obj1 = dict(name="Yann", age=25, sex="Male")
obj2 = dict([("name", "Yann"), ("age", 25), ("sex", "Male")])  # 元组列表
obj3 = {x: x + ":Good" for x in ("name", "age")}
obj4 = obj1
# print(obj1 is not obj2) # True
# print(obj1 is obj4) # True
# print(id(obj1), id(obj2), id(obj4))


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
