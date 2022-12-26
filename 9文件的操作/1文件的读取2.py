import time

with open("测试3.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
# 当执行完读取之后with函数自动将文件关闭不再占用，同时执行中出现问题不影响关闭
# 自动执行close方法
time.sleep(50000)
# 冻结文件50000秒
