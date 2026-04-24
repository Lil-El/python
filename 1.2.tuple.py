# tuple 元素不允许修改

from operator import eq

tp = ()

tp1 = (1,)

tp2 = tuple([1])

print(eq(tp1, tp2))

tp = tuple("Hello")

tp = ("1", "2", 3, 4, 5, 2)

tp = tp[0:3] + tp[4:]

tp = 1, 2, 3, 4, 5

tp = tp, (9, 10)

t1, t2 = (tp, (11, 12)), tp * 2

# 不允许删除单个元素
try:
    del tp[0]
except TypeError as e:
    print(e)

# 不允许修改单个元素
try:
    tp[0] = 3
except TypeError as e:
    print(e)

del t1
