class Animal:
    name = "animal"

    # 私有属性
    __weight = 0

    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print("I am an animal")

    def a():
        print("a")


animal = Animal("dog")


# 继承
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    # 覆盖
    def who_am_i(self):
        print("I am a dog")

    def b():
        print("b")


class SB(Dog, Animal):
    del_obj = Animal("cat")

    def __init__(self, name):
        super().__init__(name)

    # 删除对象
    def __delete__(self, name):
        print(f"正在删除属性对象: {name}")

    # 删除属性
    def __delattr__(self, name):
        print(f"正在删除属性: {name}")

    def __add__(self, other):
        return self.name + other.name

    def __repr__(self):
        # return super().__repr__()
        return f"SB(name='{self.name}')"

    def __eq__(self, value):
        if not isinstance(value, SB):
            return False
        return self.name == value.name


# print(Dog("dog2").name)

sb = SB("dog")
sb1 = SB("dog1")

# print(sb + sb1)

del sb1.name

del sb1.del_obj

# print("repr用于完整对象日志记录：" + repr(sb))

# sb1 = eval(repr(sb))
# print("搭配eval可以重新创建对象：", sb1.name)

# print(sb1 == sb, sb1 is sb)
