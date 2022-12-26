"""
函数是组织好的可以重复使用实现特定功能的代码
"""
name = "itheima"
length = len(name)  # len计算字符长度
print(length)

str = "itheima"
count = 0
for i in str:
    count += 1
print(f"字符串{str}长度, {count}")  # for循环计算繁琐
