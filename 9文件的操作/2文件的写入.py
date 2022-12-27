import time  # 导入包
f = open("测试/测试写入.txt", "w", encoding="UTF-8")
# 打开文件
f.write("hello word!!")  # 如果没有文件会创建一个，内容写入到内存中，如果文件存在再次写入会讲文件清空
# write写入
f.flush()  # 内容刷新到硬盘
# flush刷新
# time.sleep(60000)
# 冻结
f.close()  # 关闭文件占用，并且close内置flush

with open("测试/测试写入.txt", "w", encoding="UTF-8")as f1:
    f1.write("别骂了")
# with写入
f1 = open("测试/测试写入.txt", "r", encoding="UTF-8")
print(f1.read())