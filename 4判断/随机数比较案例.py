import random
num = random.randint(1, 10)
one = int(input("请猜第一次"))
if one != num:
    if one - num > 0:
        print("猜大了")
    else:
        print("猜小了")
    two = int(input("请猜第二次"))
    if two != num:
        if two - num > 0:
            print("猜大了")
        else:
            print("猜小了")
        three = int(input("请猜第三次"))
        if three != num:
            if three - num > 0:
                print("猜大了")
            else:
                print("猜小了")
            print(f"失败num的值为{num}")
        else:
            print("猜对啦")
    else:
        print("猜对啦")
else:
    print("猜对了")