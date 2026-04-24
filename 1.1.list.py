from random import random as rd, choice as ch, shuffle

arr = [1, 2, 3, 4, 5]
arr = list(range(0, 10, 2))  # 0 2 4 6 8
arr = [x + 1 for x in arr]  # 1 3 5 7 9
arr = [
    [x, x**2] for x in arr if (x + 1) % 2 == 0
]  # [[1, 1], [3, 9], [5, 25], [7, 49], [9, 81]]
print(arr)

""""""
""""""
""""""

arr = [i + 1 for i in range(len(arr))]  # 1 2 3 4 5

for i, v in enumerate(arr):
    print(v, end="*" if i < len(arr) - 1 else "\n")  # 三元运算

shuffle(arr)  # 随机排序

arr.append(6)
arr.remove(6)
arr.sort()  # 修改原列表，不返回新的列表
arr += [6] + [7, 8] * 2
arr[0:2] = [-2, -1]
del arr[0:2]

print(arr)
print(min(arr))
print(sum(arr))

arr = [[x for x in range(0, i)] for i in range(1, 5)]

print(arr)

a = ["name", "age"]
b = ["Yann", 18]

for k, v in zip(a, b):
    print(f"{k} is {v}.")
    print("%s is %s" % (k, v))
