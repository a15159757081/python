# 传入参数的功能是：在函数计算的时候，接受外部调用
def i(x, y):  # 可以传入任意数量的参数
    num = x + y
    print(f"{x}+{y}={x + y}")
    return 0


i(10, 20)  # 在调用函数时指定前面传入参数的值


# 练习
def tw(z):
    if z <= 37.5:
        print("欢迎来到宝宝巴士！请配合测量体温\n体温测量中，您的体温是：%.1f度，体温正常请进！" % z)
    else:
        print(
            "欢迎来到宝宝巴士！请配合测量体温\n体温测量中，您的体温是：%.1f度，体温异常需要隔离！" % z)


tw(float(input("后台输入体温")))