# 基本逻辑
f = open("测试/测试追加.txt", "a", encoding="UTF-8")
# 使用a(写入)模式打开文件
f.write("\n陈奕迅苦瓜也好听")
# 写入信息
f.flush()
# 刷新数据到硬盘（未刷新则数据存储在内存中）
f.close()
# 解除文件占用，内置flush函数
with open("测试/测试追加.txt", "a",encoding="UTF-8") as f1:
    f1.write("\n周杰伦你怎么连话都说不清楚")
with open("测试/测试追加.txt", "r", encoding="UTF-8")as f2:
    print(f2.read())