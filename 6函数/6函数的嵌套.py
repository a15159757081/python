# 所谓的函数嵌套就是指一个函数里面又调用了另外一个函数
def one():
    print("好的")


def two():
    print("答应我别说话")

    one()

    print("不是和你说了别说话吗？")


two() # 调用函数