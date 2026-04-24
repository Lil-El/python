arr = list((1, 2))

# 迭代器
it = iter(arr)

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break

for i in iter(arr):
    print(i, end=" ")

print("\n============================\n")


# 生成器
def fibonacci(n):
    a, b, count = 0, 1, 0
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        break
