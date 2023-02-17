class Student:
    name = None

    def sey_hi(self):
        print(f"大家好，我是{self.name},欢迎大家多多关照")

    def sey_hi2(self, msg):
        print(f"大家好我是{self.name},{msg}")


stu_1 = Student()  # 创建对象
stu_1.name = "周杰伦"  # 使用成员变量并且赋值
stu_1.sey_hi2("哎呦不错哦")  # 使用方法

stu_2 = Student()  # 创建对象
stu_2.name = "林俊杰"  # 使用成员变量并且赋值
stu_2.sey_hi2("小伙子我看好你")  # 使用方法
