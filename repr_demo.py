"""
Python 中 repr() 函数的使用示例

repr() 函数返回对象的"官方"字符串表示，通常用于调试和开发。
与 str() 不同，repr() 的目标是明确无歧义，理想情况下应该能用来重新创建对象。
"""

# ==================== 1. 基本数据类型的 repr ====================
print("=" * 50)
print("1. 基本数据类型的 repr")
print("=" * 50)

# 字符串
text = "Hello, World!"
print(f"原始字符串: {text}")
print(f"str():      {str(text)}")
print(f"repr():     {repr(text)}")
print(f"区别: repr 包含引号，显示原始字符串形式")
print()

# 数字
num = 42
print(f"数字: {num}")
print(f"str():  {str(num)}")
print(f"repr(): {repr(num)}")
print()

# 浮点数
pi = 3.14159
print(f"浮点数: {pi}")
print(f"str():  {str(pi)}")
print(f"repr(): {repr(pi)}")
print()

# 布尔值
flag = True
print(f"布尔值: {flag}")
print(f"str():  {str(flag)}")
print(f"repr(): {repr(flag)}")
print()

# None
none_val = None
print(f"None: {none_val}")
print(f"str():  {str(none_val)}")
print(f"repr(): {repr(none_val)}")
print()


# ==================== 2. 容器的 repr ====================
print("=" * 50)
print("2. 容器的 repr")
print("=" * 50)

# 列表
my_list = [1, 2, 3, "hello"]
print(f"列表: {my_list}")
print(f"repr(): {repr(my_list)}")
print()

# 字典
my_dict = {"name": "Alice", "age": 25}
print(f"字典: {my_dict}")
print(f"repr(): {repr(my_dict)}")
print()

# 集合
my_set = {1, 2, 3}
print(f"集合: {my_set}")
print(f"repr(): {repr(my_set)}")
print()

# 元组
my_tuple = (1, 2, 3)
print(f"元组: {my_tuple}")
print(f"repr(): {repr(my_tuple)}")
print()


# ==================== 3. 特殊字符的显示 ====================
print("=" * 50)
print("3. 特殊字符的显示")
print("=" * 50)

# 换行符
text_with_newline = "Hello\nWorld"
print(f"包含换行符的字符串:")
print(f"str():  {str(text_with_newline)}")
print(f"repr(): {repr(text_with_newline)}")
print(f"说明: repr 显示 \\n 而不是实际换行")
print()

# 制表符
text_with_tab = "Hello\tWorld"
print(f"包含制表符的字符串:")
print(f"str():  {str(text_with_tab)}")
print(f"repr(): {repr(text_with_tab)}")
print()

# 引号
text_with_quote = 'He said "Hello"'
print(f"包含引号的字符串:")
print(f"str():  {str(text_with_quote)}")
print(f"repr(): {repr(text_with_quote)}")
print()


# ==================== 4. 自定义类中的 __repr__ ====================
print("=" * 50)
print("4. 自定义类中的 __repr__")
print("=" * 50)

class Person:
    """一个简单的 Person 类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        """返回对象的官方字符串表示"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __str__(self):
        """返回对象的友好字符串表示"""
        return f"{self.name}, {self.age}岁"

# 创建 Person 对象
person = Person("张三", 30)

print(f"Person 对象:")
print(f"print(person):   {person}")
print(f"str(person):     {str(person)}")
print(f"repr(person):    {repr(person)}")
print()

# 在列表中显示
people = [Person("李四", 25), Person("王五", 35)]
print(f"Person 对象列表:")
print(f"print(people):   {people}")
print(f"repr(people):    {repr(people)}")
print(f"说明: 容器中使用的是每个元素的 __repr__")
print()


# ==================== 5. repr 的实际应用场景 ====================
print("=" * 50)
print("5. repr 的实际应用场景")
print("=" * 50)

# 场景1: 调试时查看变量的准确值
print("场景1: 调试")
debug_text = "test\nvalue"
print(f"调试信息 - 变量值: {repr(debug_text)}")
print()

# 场景2: 日志记录
print("场景2: 日志记录")
log_data = {"user": "admin", "action": "login\ttime"}
print(f"日志: {repr(log_data)}")
print()

# 场景3: 生成可执行的代码字符串
print("场景3: 生成可重建对象的代码")
sample_list = [1, 2, 3]
repr_str = repr(sample_list)
print(f"repr 字符串: {repr_str}")
reconstructed = eval(repr_str)
print(f"重建的对象: {reconstructed}")
print(f"是否相等: {sample_list == reconstructed}")
print()


# ==================== 6. str vs repr 对比总结 ====================
print("=" * 50)
print("6. str vs repr 对比总结")
print("=" * 50)

class Example:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"用户友好的显示: {self.value}"
    
    def __repr__(self):
        return f"Example(value={self.value!r})"

obj = Example("测试")
print(f"对象: {obj}")
print(f"str(obj):  {str(obj)}")
print(f"repr(obj): {repr(obj)}")
print()
print("总结:")
print("- str(): 面向用户，易读，用于 print 和 str()")
print("- repr(): 面向开发者，明确无歧义，用于调试和 repr()")
print("- 在容器中（列表、字典等），元素使用 __repr__")
print("- 理想情况下，eval(repr(obj)) 应该能重建对象")
