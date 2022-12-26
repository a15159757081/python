# 容器集合的使用
# 集合的定义
my_set = {"周杰伦", "林俊杰", "薛之谦", "周杰伦", "林俊杰", "薛之谦", "周杰伦", "林俊杰", "薛之谦"}
my_set_empty = set()  # 定义空集合
print(f"my_set的内容是{my_set},类型是：{type(my_set)}")
print(f"my_set_empty,内容是{my_set_empty},类型是{type(my_set_empty)}")
# 通过代码得知集合不能重复同时是无序的

# 添加新元素
my_set.add("陈奕迅")
my_set.add("周杰伦")  # 去重所以不会添加上去
print(f"my_set添加元素后的结果是：{my_set}")

# 移除元素
my_set.remove("林俊杰")
print(f"移除之后的结果为{my_set}")

# 随机取出一个元素
name = my_set.pop()  # 随机取出一个元素放入变量中，因为集合没有下标所以说没有参数
print(f"取出元素后集合为{my_set},取出的元素是{name}")

# 清空集合.clear
my_set.clear()
print(f"集合被清空了结果是{my_set}")

# 取出两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1合set2的差集是{set3}")
print(f"集合1为{set1}")
print(f"集合2为{set2}")  # 计算差集不会更改源集


# 消除2的集合的差集(留相同的集合)
set1.difference_update(set2)
print(f"消除差集后得到，集合1结果{set1}")
print(f"消除差集后得到，集合2结果{set2}")  # 集合2是没有变化的只是去除了集合1的差集

# 合并集合.unior
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"两集合合并后集合3{set3}")
print(f"合并后集合1{set1}")
print(f"合并后集合2{set2}")  # 也就是合并后返回一个新的集合，原来的两个集合没有变化

# 计算集合的元素数量len()
set1 = {1, 2, 3, 4, 5, 6}
num = len(set1)
print(f"集合里面有{num}元素")


# 集合的遍历
# 集合不支持下标索引，不能用while
# 可以用for循环
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合中的元素有：{element}")

# 练习
my_list = ['黑马程序员', '传智播客', 'iteima', 'itcast', 'iteima', 'itcast', 'best']
my_list1 = set()
for i in my_list:
    print(f"集合的元素有{i}")
    my_list1.add(i)
print(f"存入的集合去重后有{my_list1}")