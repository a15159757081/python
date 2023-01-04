mun = [10, 1, 3, 2, 5, 4, 9, 7, 8, 6]  # 定义一个列表
count = len(mun)  # 计算列表长度，下标为1
for i in range(count):  # 比较的次数
    for j in range(count-1-i):  # 循环0~9，一共9次
        if mun[j] > mun[j+1]:  # j的值不超过8才不会下标越界
            a = mun[j]
            mun[j] = mun[j+1]
            mun[j+1] = a
       # 计算循环取得的第几个较大值

print(mun)
"""
每次比较都会产生一个数组内最较大值，
这个较大值后面的比较中就不需要比较了
第一个循环为比较的次数，每次循环完成出现一个较大值range下标为0
"""