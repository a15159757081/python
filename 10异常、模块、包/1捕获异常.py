"""
基本语法
Try：
    可能发生错误的代码
Except：
    如果发生错误执行的代码
else：（可选）
    如果没有异常执行的代码
finally: (可选)
    有没有异常都会执行的代码
"""
try:
    f = open("测试文件/linux.txt", "r", encoding="UTF-8")
except:
    print("文件不存在，我将改为w模式")
    f = open("测试文件/linux.txt", "w", encoding="UTF-8")

# 捕获指定异常
try:
    print(name)
    # 1/0
except NameError as e:
    # 这里捕获的异常为NameError也就是变量未定义，其他异常无法捕获，这里的e表示异常信息
    print(f"出现了变量为未定义异常{e}")

# 捕获多个异常
try:
    # print(name)
    1 / 0
except(NameError, ZeroDivisionError) as e:
    # 这里捕获的异常为NameError也就是变量未定义，其他异常无法捕获，这里的e表示异常信息
    print(f"出现了变量为未定义异常或1/0异常{e}")  # 因为从上到下执行所以捕获到的异常信息为第一个错误信息

# 捕获所有异常(也可使用最上面的基础语法)
try:
    1 / 0
except Exception as e:  # Exception顶级异常
    print("出现异常")

# else语句
try:
    6 / 3
except Exception as e:  # Exception顶级异常
    print("出现异常")
else:
    print("恭喜你没有出现异常")

# finally语句
try:
    f = open("测试文件/linux1.txt", "r", encoding="UTF-8")
except:
    print("文件不存在，我将改为w模式")
    f = open("测试文件/linux1.txt", "w", encoding="UTF-8")
else:  # （没有异常执行）
    print("没有异常")
finally:  # (有无异常都会执行)
    f.close()