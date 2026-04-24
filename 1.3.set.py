st = {"10", "20", "30", "40", "50"}  # 无序不重复

st.add(4)  # st + set(2) 不允许修改
# print("4 in st:", 4 in st)

st.update({1, 3}, (2, 3))
# print(st)

st.remove(3)  # 不存在就报错
st.discard("10")  # 不存在不报错
# print('"10" not in st:', "10" not in st)

st.pop()  # 随机删除一个元素

for i in st:
    if i == 4:
        break
    elif i == 2:
        continue
    else:
        pass  # 仅占位，不影响后续代码执行

st = ()
# print(type(st)) # tuple
st = {}
# print(type(st)) # dict
st = set()
# print(type(st)) # set
st = set("hello")
# print(st) # set {'h', 'l', 'e', 'o'}
st = set(("world",))
# print(st) # set {"world"}
st = set(("hello", "world"))
# print(st) # set {"hello", "world"}


# 集合运算
print(st - set(("world",)), st & set(("world",)))
print(st & set("world"))  # {hello world} & {w o r l d}
print(st | set("world"))  # {hello world} | {w o r l d}

# 反序遍历
for f in reversed(sorted(set("hello"))):
    print(f)


# 集合推导式
st = {x for x in "hello" if x not in "aeiou"}
# print(st) # set {'h', 'l'}
