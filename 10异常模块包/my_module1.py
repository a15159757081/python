def test(a, b):
    print(a + b)
    return 0

test(1, 2)
print(__name__)
if __name__ == "__main__":
    test(1, 2)
"""
也就是说__name__这个内置变量在当前模块中等于__main__
但是当其他地方调用当前模块时，__name__的值就会变为被调用模块的模块名
作用：
    当我们想要测试这个模块但是测试完不想把代码删除
    或者是我们想让这个模块可以单独拿出来使用
"""