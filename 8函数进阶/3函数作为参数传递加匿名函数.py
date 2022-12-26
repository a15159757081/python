def text_func(cc):  # 传入函数，也就是代码执行的逻辑，这里的函数类似于数据的载体
    a = cc(1, 2)  # 使用变量接收函数，因为使用了函数所以要在函数内加传入的参数，此时函数只有数值没有逻辑
    print(a)
    return 0


def aa(x, y):
    return x + y  # 函数的返回值问接收的两个变量的和


text_func(aa)  # 这里调用的其实是参数的逻辑

text_func(lambda x, y: x + y)  # 将值给入变量并在冒号后表示逻辑
# lambda函数的使用，一次性无法再次使用，使用简单避免控件浪费
