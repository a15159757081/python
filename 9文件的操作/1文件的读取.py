f = open("D:/测试.txt", "r", encoding="UTF-8")
print(type(f))
print(f"读取1个字节为：{f.read(1)}")
# read方法可以指定读取文件的数据长度，如果没有传入参数则默认读取全部数据

lines = f.readlines()  # 读取数据并存入列表中
print(f"数据变量为{type(lines)}")
a = lines[0]
print(a)
# 如果在程序中多次调用read则下次的read会在上一个read的结尾处继续读写
