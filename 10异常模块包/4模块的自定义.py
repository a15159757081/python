# 导入自定义模块的使用
import my_module2

my_module2.test(3, 2)  # test为模块内部的函数名


# 模块的注意事项
from my_module1 import test  # 变灰表示没有被使用
"""
但是模块内部写了函数的调用，当我们调用模块的时候则自动使用，也就是调用模块的时候回执行一次模块内容,内容为3
并且输出__name__变量
"""
from my_module2 import *

test(1, 2)
# 注意：当调用模块内部函数并导入多个模块同名模块的时候，调用的是最后导入的模块