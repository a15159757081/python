"""
演示异常具有传递性
演示：
    异常通过函数的传递一步一步传递
"""


# 定义一个函数
def func1():
    print("执行开始")
    num = 1 / 0
    print("执行结束")


# 定义第二个函数
def func2():
    print("执行开始")
    func1()
    print("执行结束")


# 定义第三个函数
def main():
    try:
        func2()
    except Exception as a:
        print(f"有问题，问题为{a}")


main()