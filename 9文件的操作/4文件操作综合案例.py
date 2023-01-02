fr = open("测试/bill.txt", "r", encoding="UTF-8")
fw = open("测试/bill.txt.bak", "a", encoding="UTF-8")
for line in fr:
    line = line.strip()
    if line.split(",")[-1] == "测试":  # 这里可以使用not则只需要判断一次
        continue
    else:
        fw.write(line)
        # 由于前面的换行符被删除所以手动写入换行符
        fw.write("\n")
fr.close()
fw.close()  # 自动调用flush
"""
基本思路：
打开两个文件
使用循环读取要备份的文件
将读取到的每一行使用逗号划分列表并删除前后空格及换行
使用下标确定判断位置并判断
判断完毕输入
关闭文件
"""