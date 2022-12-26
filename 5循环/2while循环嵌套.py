# 外层循环表白100天，内层循环送10朵玫瑰花
i = 1
mg = 0
while i <= 100:
    print(f"今天第{i}天去表白")
    j = 1
    while j < 10:
        j += 1
    mg += j
    print(f"一共送给小美{mg}朵玫瑰")
    i += 1