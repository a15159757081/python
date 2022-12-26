import random

money = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    if money == 0:
        print("工资发完了下个月领取吧")
        break
        # 判断余额情况

    if num < 5:
        print(f"员工{i}绩效分{num},低于5，不发工资，下次一定")
        continue     # 不符合条件直接跳过
    money -= 1000
    print(f"向员工{i}发放工资1000元，账户余额还剩{money}元。")