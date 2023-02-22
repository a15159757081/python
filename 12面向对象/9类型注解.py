# 基础数据类型注解（类似于定义变量）
import json
import random

var_1: int = 10
var_2: str = "itheima"
var_3: bool = True


# 对象类型注释
class Student:
    pass


stu: Student = Student()
# 容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"周杰伦": 666}
# 容器类型详细注解
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, str] = (1, "2")  # 元组需要把所有的元素类型注释出来
my_dict1: dict[str, int] = {"周杰伦": 666}

var1: random.randint(1, 10)  # type: int  # 通过注释注释数据类型
var2: json.loads('{"name":"zhangshan"}')  # type: dict[str, str]


def func():
    return 10


var3: func()
