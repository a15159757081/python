# 将容器内的元素依次取出进行处理的行为，称为：遍历、迭代
def list_while_func():
    my_list2 = ["真的好累", "改干什么呢", "累就休息一会"]
    num = 0
    while num < len(my_list2):  # 这里len计算出来的数量下标为1，而列表下标为0所以说只需要小于列表下标就好了
        element = my_list2[num]
        print(f"列表的元素：{element}")
        num += 1


list_while_func()  # while循环的方法


def list_for_func():
    my_list1 = [1, 2, 3, 4, 5]
    for i in my_list1:  # 因为for循环的机制我们吧数组的每一个值都加入i这个时候输出i就行了
        print(f"for循环输出元素{i}")


list_for_func()


# 练习
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_new = []
my_new1 = []
a = 0


def list_one():
    global my_new
    num = 0
    while num < len(my_list):
        if my_list[num] % 2 == 0:
            my_new.append(my_list[num])
        num += 1
    print(my_new)


list_one()


def list_two():
    global my_new1
    for i in my_list:
        if i % 2 == 0:
            my_new1.append(i)
    print(my_new1)


list_two()

