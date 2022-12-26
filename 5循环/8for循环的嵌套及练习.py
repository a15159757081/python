# i = 1
# for i in range(1,101):
#     print(f"今天是表白小美的第{i}天")
#     for j in range (1, 11):
#         print(f"送小美的第{j}朵花")
#     print(f"小美,我喜欢你{i}天")
# print(f"第{i}天，表白成功")

# 练习
for i in range(0, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end='')
    print()
