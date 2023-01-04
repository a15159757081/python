# 定义函数进行文档说明


def add(x, y):
    """
    add可以接受两个函数并相加
    :param x:形参x为相加其中的一个函数
    :param y:形参y为相加另一个函数
    :return:返回的2数相加的结果
    """
    num = x + y
    print(f"计算的值为{num}")
    return num


add(10, 20)