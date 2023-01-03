"""
python的模块导入(一般写在文件开头的位置)
基本语法：（使用时大括号可省略）
    【for模块名】 import 【模块|类|变量|函数|*】【as别名】
"""

# 导入模块第一种方式
import time  # 导入python内置的模块（time.py这个代码文件）

print("你好")
time.sleep(5)  # 点也就是sleep是属于time这个模块的，层级关系，sleep睡眠
print("我好")

# 第二种
from time import sleep  # 直接从time中导入sleep使用

sleep(5)  # 此时直接使用sleep就行

# 所以*导入time中的全部模块
from time import *  # * 表示全部的意思  # 这种写法和第一种的区别是使用时不用写time.sleep直接写sleep
sleep(3)
print("休息3秒")

# 使用as给特定功能加上别名
import time as t  # 也就是相当于把模块重命名或者是重新定义了
t.sleep(3)
from time import sleep as sl
sl(3)