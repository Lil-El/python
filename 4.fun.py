def hello(name, age, sex="Male"):
    print("Hello, %s, you are %d, you are %s" % (name, age, sex))


hello("Yann", 28)

hello("Jiwon", 32, "Female")

hello(name="Mino", age=30)


def calc(*args):
    c = 0
    for i in args:
        c += i
    return c


print(calc(1, 2, 3, 4, 5))
