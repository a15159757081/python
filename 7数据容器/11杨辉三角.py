a = [1]
# for i in range(10):
#     print(a)
#     a.append(0)
#     a = [a[k]+a[k-1] for k in range(i + 2)]

list1 = []
list2 = []
num = int(input("输入行数"))
for i in range(num):
    if i == 0 or i == 1:
        list1.append(1)
        print(list1)
    else:
        for j in range(i+1):  # 因为j代表的是行位数，当j是第一个或最后一个的时候为1
            if j == 0:
                list2 = [1]
            elif j == i:
                list2.append(1)
            else:
                num1 = list1[j-1] + list1[j]
                # j这个时候位数不是第一位也不是最后一位则会将上一个数列出头开始和下一位开始相加，相加的关系就是每一位减去1加上当前位数
                list2.append(num1)
        list1 = list2
        print(list1)

