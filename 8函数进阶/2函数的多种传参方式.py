def aa(name, age, xb):
    print(f"我叫{name}，性别{xb}今年{age}岁")
    return 0


def bb(name, age, xb):
    print(f"我叫{name}，性别{xb}今年{age}岁")
    return 0


def cc(name, age, xb='男'):  # 传入默认参数，传入的默认参数要写在最后面
    print(f"我叫{name}，性别{xb}今年{age}岁")
    return 0


def dd(*args):  # args为规范可以自行定义
    print(f"args的类型为{type(args)}", args)


def dd1(**kwargs):
    print(f"kwargs的数据类型是{type(kwargs)}", kwargs)


aa("小王", 6, "男")
# 位置参数,根据插入参数的顺序
bb(age=6, name="小王", xb="男")  # 可以不按固定顺序
bb("小王", age=6, xb="男")  # 可以和位置参数混用但是位置参数必须放前面
# 关键字参数，调用时通过键=值形式传递
cc("小明", 8)
cc("小明", 8, "女")
# 缺省参数，在定义函数阶段传入的参数可以不在使用时传入，并且可以在传入时更改
dd("aa", "bb", "cc")
# 通过*号传递不定长参数，这种参数被称为位置传递,插入的类型问元组
dd1(aa=1, bb=2, cc=3)