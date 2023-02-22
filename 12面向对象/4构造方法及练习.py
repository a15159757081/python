# 构造方法的名称__init__
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):  # __init__自动执行
        self.name = name  # 这里既有赋值的功能也有定义的功能，上面可以省略
        self.age = age
        self.tel = tel
        print("Student创建了一个类对象")


# sut = Student("周杰伦", 31, "15559039490")
# print(sut.name)
# print(sut.age)
# print(sut.tel)

class Std1:
    name = None
    age = None
    add = None

    def __init__(self):
        count = int(input("请输入创建学生的个数："))
        for i in range(1, count + 1):
            print(f"当前录入学生{i},总共需录入{count}个学生")
            self.name = input("请输入学生姓名：")
            self.age = input("请输入学生年龄：")
            self.add = input("请输入学生地址：")
            print(f"学生{i}信息录入完成，信息：【学生姓名：{self.name},年龄{self.age}，地址{self.add}】")


std1 = Std1()
