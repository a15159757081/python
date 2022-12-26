# 切片语法：序列[起始下标:结束下标:步长]
"""
起始下标留空表示从头开始
结束下标留空表示截取到结尾
步长表示取值的间隙
"""
# 对list进行切片，从1开始，4结束，步长1
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]  # 步长默认是一可以省略不写
print(f"结果为{result1}")

# 对tuple进行切片，从头开始，最后结束，步长1
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # 起始和结束不写，步长为1可以省略所以最后写一个冒号就行
print(f"结果为{result2}")

# 对str进行切片，从头开始，最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果为{result3}")

# 对str进行切片，从头开始，最后结束，步长-1
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果为{result4}")  # 等同于讲序列反转了

# 对列表进行切片，从3开始，1结束，步长-1
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"结果为{result5}")

# 对元组进行切片，从头开始，最后结束，步长-2
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果为{result6}")

# 练习
my_str = "万过薪月，员序程马黑来，nohtyp学"
now_my_str = my_str[9:4:-1]
print(f"改完后得到{now_my_str}")
# 方法二
now_my_str = my_str.split("，")[1].replace("来", "")[::-1] # 注意字符串的逗号是中文
print(now_my_str)