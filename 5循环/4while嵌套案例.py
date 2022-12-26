"""
print不换行 ,end=''
\t效果等同于TAB
"""
print("我真的", end='')
print("很累")
print("累\t了就休息一下")
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t", end='')
#         j += 1
#     i += 1
#     print()

i = 1
j = 1
while i <= 9:
    n = 0           # 根据规律得知行数+输出个数为10，n用来判断输出的个数
    x = 0           # 用来计算行数加输出个数的和
    j = i           # 用来定位第一个数因为第一个数为行数
    while n < 10:
        print(f"{i}*{j}={i * j}\t", end='')
        j += 1
        x += 1
        n = x + i
    i += 1
    print()