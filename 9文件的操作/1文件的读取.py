f = open("测试.txt", "r", encoding="UTF-8")
print(type(f))
print(f"读取1个字节为：{f.read(1)}")
# read方法可以指定读取文件的数据长度，如果没有传入参数则默认读取全部数据

# print(f.read())
# 如果在程序中多次调用read则下次的read会在上一个read的结尾处继续读写

lines = f.readlines()  # 读取数据并存入列表中
print(f"数据变量为{type(lines)}")
print(lines)  # 他也会续接上一个读取数据的位置，此时数据读取完毕则输出的空
# 输出时候的\n代表换行，并且每一行为一个列表项

f1 = open("测试2.txt", "r", encoding="UTF-8")
print(f"第一行数据:{f1.readline()}")
print(f"第二行数据:{f1.readline()}")
print(f"第三行数据:{f1.readline()}")
# readline表示输出一行

f2 = open("测试3.txt", "r", encoding="UTF-8")
for line in f2:
    print(line)
# 循环读取文件,每一次读取每一行
f2.close()
# 解除文件占用，此时运行程序的时候可以修改之前被调用的文件