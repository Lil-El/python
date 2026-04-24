from operator import eq as eqq
import math
import sys

# 导入自己的模块
# from utils import *
import utils
import tools.div

print(eqq(1, 1))

print(math.sqrt(4))

"""
python .\5.module.py -name yann -age 18

['.\\5.module.py', '-name', 'yann', '-age', '18']
"""
print(sys.argv)

calc = utils.calc

print(dir(utils))  # 模块内定义的所有名称
print(calc.__name__, "->", calc(1, 2))
print(utils.multiply.__name__, "->", utils.multiply(1, 2))
print(tools.div.div.__name__, "->", tools.div.div(1, 2))

if __name__ == "__main__":
    print("程序 %s 正在运行" % __file__)