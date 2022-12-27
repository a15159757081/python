# 字符串是字符的容器，一个字符串可以存放任意数量的字符

my_str = "周杰伦林俊杰"
# 通过下标索引取值
value = my_str[2]
value1 = my_str[-4]
print(f"从字符串{my_str}取下标为2的值为{value},取下标为-4的值为{value1}")

# 字符串同元组一样是不可修改的数据容器
# my_str[2] = "纶"

# index方法
value = my_str.index("杰")
print(f"杰在字符串{my_str},的下标是{value}")

# 字符串的替换，本质上得到是一个新的字符串他是有返回值的，数据是可读的
now_my_str = my_str.replace("周杰伦", "薛之谦")  # 因为字符串是不能修改的所以说要用一个变量去存储替换后的字符串
print(f"讲字符串替换之后得到{now_my_str}")

# 字符串的分割
my_str = "hello word"
my_str_list = my_str.split(" ")
print(f"字符串分割之后{my_str_list}，类型为{type(my_str_list)}")  # 字符串分割之后就转换为列表类型

# strip方法
my_str = " 周杰伦，林俊杰 "
new_my_str = my_str.strip()  # 不传入参数取出首位空格(取出首尾的回车换行符)
print(f"字符串{my_str}被strip之后，结果为{new_my_str}")

my_str = "12周杰伦林俊杰12"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip内传入参数后结果为{new_my_str}")
# strip传入参数后会去除首尾的字符串，不限位数

# 统计字符串中字符串出现的次数
my_str = "周杰伦，林俊杰"
num = my_str.count("杰")
print(f"杰出现的次数为{num}")

# 统计字符串的长度
long = len(my_str)
print(f"字符串的长度为{long}")


# 练习
print("—————————练习———————————")
lx = "itheima itcast boxuege"
num = lx.count("it")
print(f"一共有{num}个it")
now_lx = lx.replace(" ", "|")
print(f"空格替换竖杠后{now_lx}")
now1_lx = now_lx.split("|")
print(f"按照|进行字符串分割得到{now1_lx}")