def str_reverse(s):
    """
    这个是字符串完成反转
    :param s:讲被反转的字符串
    :return:
    """
    return s[::-1]


def substr(s, x, y):
    """
    功能是按照指定的下标完成字符串切片
    :param s:即将切片的字符串
    :param x:切片开始上标
    :param y:切片完成下标
    :return:切片完成的字符串
    """
    return s[x:y]


if __name__ == "__main__":
    print(str_reverse("好可爱"))
    print(substr("真的好可爱哦", 1, 3))