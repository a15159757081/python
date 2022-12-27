def add(x, y):
    return x + y


num = add(10, 20)


# 函数使用

class student:
    def add(self, x, y):
        return x + y


student = student()
num1 = student.add(1, 2)

# 方法的使用

lb = ["b", "b", "d", "e"]
print(f"列表初始为{lb}")
num2 = lb.index("b")
print(f"阿伟在列表的索引为{num2}")
# 列表的查找

lb[0] = "a"
print(f"列表修改后{lb}")
# 列表的修改

lb.insert(2, "b1")
print(f"添加完后的列表{lb}")
# 列表的插入

lb.append("f")
# 列表追加单个元素
lb.extend(["g", "h"])
# 列表追加多个个元素
print(f"追加元素后列表为{lb}")

del lb[0]
print(f"列表删除第一个元素为{lb}")
# 语法一删除列表
lb1 = lb.pop(2)
print(f"通过pop方法移除取出列表为{lb}被pop删除的列表元素为:{lb1}")
# 语法二删除列表，这个语法可以用变量去接收他相当于把元素取出来加入一个变量
lb.remove("b")
print(f"删除元素b之后的列表{lb}")
# 语法三通过从左到右匹配第一次元素并删除

lbsy = [1, 2, 3, 4, 1]
lbsy.clear()
print(f"列表被清空了{lbsy}")
# 清空列表

print(lb.count("b"))
# 计算该元素在列表里面出现了几次

print(f"列表元素数量一共有{len(lb)}")

# 练习
student = [21, 25, 21, 23, 22, 20]
student.append(31)
print(f"追加数字31后列表为{student}")
student.extend([29, 33, 30])
print(f"最加列表之后列表为{student}")
print(f"列表的第一个元素为{student[0]}")
print(f"列表的最后一个元素为{student[-1]}")
print(f"列表元素31的下标为{student.index(31)}")
