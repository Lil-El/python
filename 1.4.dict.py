from operator import eq

obj = {"name": "John", "age": 25}

# print(obj.keys(), obj["name"])
del obj["age"]

listKeys = list(obj.keys())

tupleKeys = tuple(obj.keys())

# print(listKeys, tupleKeys)

obj1 = dict(name="Yann", age=25, sex="Male")
obj2 = dict([("name", "Yann"), ("age", 25), ("sex", "Male")])  # 元组列表
obj3 = obj1



print("obj1 is not obj2:", obj1 is not obj2)  # True
print("obj1 eq obj2:", eq(obj1, obj2)) # True
print("obj1 == obj2:", obj1 == obj2) # True

print("====== eq和==等价，比较的是内容，is比较的是地址 ======")

print("obj1 is obj3:", obj1 is obj3)  # True
print("obj1 eq obj3:", eq(obj1, obj3))  # True
print("obj1 == obj3:", obj1 == obj3)  # True
# print(id(obj1), id(obj2), id(obj3))

# 推导式
obj = {x: x + ":Good" for x in ("name", "age")}

obj.clear()
del obj

obj = {("name"): "Yann", "age": 25}

# 不能使用列表作为字典的键
try:
    obj = {["name"]: "Y", "age": 25}
except TypeError as e:
    print(e)
