class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"姓名{self.name},年龄{self.age}"

    # __lt__魔术方法（只能用于小于，大于）
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法（可以用于大于等于）
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法（比较是否相等）
    def __eq__(self, other):  # 如果不使用eq的话默认比较的是内存地址
        return self.age == other.age


stu = Student("周杰伦", 31)
# print(stu)  # 这里在没有使用str魔术方法时只能输出函数的内存地址
stu2 = Student("林俊杰", 36)
print(stu < stu2)  # 输出小于stu2是否为True
print(stu >= stu2)  # 输出小于等于stu2是否为True
print(stu == stu2)
