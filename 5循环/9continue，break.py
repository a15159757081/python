# continue介绍
for i in range(1, 11):
    print("666")
    for j in range(1, 11):
        print("111")
        continue  # 跳过下面代码不执行,并且范围只到当前循环，一般用于跳过本次循环
        print("999")
    print("结束")

# break介绍
for x in range(1, 11):
    print("我可以显示")
    break     # 遇到后直接跳出循环
