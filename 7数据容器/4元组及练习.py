# 如果想要传递的信息不被修改列表就不合适了，这个时候就诞生了元组
"""
元组的定义：定义使用小括号，且用逗号隔开各个数据，数据可以是不同是数据类型
"""
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()  # 面向对象
t4 = (1,)
# t2,t3这里都属于是空元组
print(f"t1的类型是{type(t1)}, 内容是{t1}")
print(f"t1的类型是{type(t2)}, 内容是{t2}")
print(f"t1的类型是{type(t4)}, 内容是{t4}")
# 注意如果你的元组只有一个数据要在数据的最后面加上逗号不然就不是元组类型了


# 元组的嵌套
t5 = ((1, 2, 3), (4, 5, 6))
print(t5)

# 下标索引取出内容
print(t5[1][2])

# 元组的操作： 查找下标
t6 = ("说了再见", "分裂", "借口", "借口")
name = t6.index("分裂")
print(f"分裂的下标是{name}")

# 元组的操作： count统计方法
num = t6.count("借口")
print(f"统计的借口数量为{num}")

# 元组的操作： len函数计算元组元素数量
num1 = len(t6)
print(f"元组一共有{num1}个")

index = 0
while index < len(t6):
    print(f"元组的元素有{t6[index]}")
    index += 1

for element in t6:
    print(f"元组的元素有{element}")

# 修改元组内容
# t6[0] = "dad" 元组无法修改

# 定义一个包含列表的元组
ta = (1, 2, 3, [0, 6, 7])
ta[3][1] = 1

# 练习
yz = ('周杰伦', 11, ["football", 'music'])
num = yz.index(11)
print(f"年龄的下标为{num}")
name = yz.count("周杰伦")
print(f"查询有无周杰伦{name}")
yz[2].remove("football")  # 这里类似于进入列表
print(f"删除football之后{yz}")
yz[2].append("coding")
print(f"添加coding后{yz}")