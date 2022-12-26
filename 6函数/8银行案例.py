money = 5000000
name = input("请输入姓名")


def ye(show):
    if show:
        print("------------余额查询------------")
    print(f"{name}，您好，您的余额剩余：{money}")


def ck():
    global money
    a = int(input("请输入存款"))
    money += a
    print("------------存款------------")
    print(f"{name}你好，您存款{a}元成功")
    ye(False)


def qk():
    global money
    if money == 0:
        print("余额不足")
    else:
        a = int(input("请输入取款"))
        money -= a
        print("------------取款------------")
        print(f"{name}你好，您取款{a}元成功")
        ye(False)


def zy():
    print(f"{name}你好，欢迎来到新加坡银行ATM，请选择操作")
    print("查询余额\t", "【输入1】")
    print("存款\t\t", "【输入2】")
    print("取款\t\t", "【输入3】")
    print("退出\t\t", "【输入4】")
    a = int(input())
    if a == 1:
        ye(True)
    elif a == 2:
        ck()
    elif a == 3:
        qk()
    else:
        global pd
        pd = 0


pd = 1
while pd:
    zy()
