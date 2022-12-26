# 定义字符串name
name = "itheima"
# for循环处理
for x in name:
    print(x)  # 得出结论for循环会把字符串逐个取出放入x临时变量进行处理

# 练习
name = "itheima is a brand of itcast"
num = 0
for y in name:
    if y == "a":
        num += 1
print(f"itheima is a brand of itcast中共有：{num}个字母a")
