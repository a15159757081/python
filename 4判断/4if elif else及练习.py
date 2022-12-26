print("欢迎来到黑马动物园")
height = int(input("请输入身高（cm）"))
if height < 120:
    print("身高小于120，您可以免费游玩")
elif int(input("请输入您的vip等级")) > 3:    # 简洁写法
    print("您的vip等级大于三可以免费游玩")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快")

# 练习
num = 10
if input("请输入第一次猜想的数：") == 10:
    print("恭喜你猜对了")
elif input("不对再猜一次：") == 10:
    print("恭喜你猜对了")
elif input("不对，最后猜一次：") == 10:
    print("恭喜你全部猜对了")
else:
    print("sorry,全部猜错了，我想的是：10")