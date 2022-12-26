# 返回值就是程序中函数完成所有事情之后，给调用者的结果

def i(x, y):
    num = x + y
    return num


# 当函数体运行到返回值时后面的代码则不生效


# 函数的返回值可以通过变量去接收
r = i(10, 20)
print(r)


# 如果函数没有使用返回语句返回数据，函数的返回值就为None
def j():
    print("你好")


result = j()
print(f"无返回值返回的内容为{result},返回的类型为{type(result)}")

a = None
if a:
    print("不可以输出")
# if后面为空字符串和0不执行
