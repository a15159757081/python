import time

with open("测试3.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
# 当执行完读取之后with函数自动将文件关闭不再占用，同时执行中出现问题不影响关闭
# 自动执行close方法
# time.sleep(50000)
# 冻结文件50000秒


# 练习
a = 0
# with open("word.txt", "r", encoding="UTF-8")as f1:
#     a = f1.read()
#     count = a.count("itheima")
# print(f"出现的次数是{count}")
# 第一种方法
words = []
count = 0  # 使用count计算数量
with open("word.txt", "r", encoding="UTF-8")as f1:
    for line in f1:
        line = line.strip()  # 不传入参数取出首行空格
        words.extend(line.split(" "))  # 因为每个单词之间用空格分开，则我们用空格分割字符串，分割完为列表
    for word in words:
        if word == "itheima":
            count += 1
print(count)