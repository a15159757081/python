# range 语法
# for x in range(10):  # 从0开始不包括10
#     print(x)
# # 语法一
# for y in range(5, 10):
#     print(y)
#
# for z in range(5, 10, 2):
#     print(z)

for x in range(10):
    print("送玫瑰花")

# 练习
o = 0
num = int(input("请输入目标数"))
for y in range(1, num):
    if y % 2 == 0:
        o += 1
print(f"1到{num}一共有{o}个偶数")