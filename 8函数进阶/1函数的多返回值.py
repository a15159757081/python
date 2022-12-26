def cc(name, age, xb):
    print(f"我叫{name}，性别{xb}今年{age}岁")
    return 0


cc(age=6, name="小王", xb="男")  # 可以不按固定顺序
cc("小王", age=6, xb="男")  # 可以和位置参数混用但是位置参数必须放前面
# 关键字参数，调用时通过键=值形式传递


def aa():
    return 1, 3, 9


a, b, c = aa()
print(a, b, c)
# 接收函数的多个返回值此时直接用函数赋值给变量就行了，函数的多返回值
