import random
num = random.randint(1, 100)
cs = 1
a = True
while a:  # while后面的值相当于是一个布尔判断当为true的时候开启
    s = int(input("请输入你要猜的数"))
    if s == num:
        print(f"猜对啦，猜了{cs}次")
        a = False
    else:
        if s - num > 0:
            print("大了")
        else:
            print("小了")
        cs += 1
