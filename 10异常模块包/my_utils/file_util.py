def print_file_info(path):
    """
    讲指定的文件路径输出内容到控制台中
    :param path:输出文件的路径
    :return:
    """
    f = None  # 设置初始值为空，也是为了下面的能正常关闭文件
    try:
        f = open(path, "r", encoding="UTF-8")
        print(f.read())
    except:
        print("文件不存在")
    finally:  # 这里可以使用else
        if f:  # 因为none默认值为flash所以没有打开文件时不会执行关闭文件
            f.close()


def append_file(path1, data):
    f = open(path1, "a", encoding="UTF-8")
    f.write(data)


if __name__ == "__main__":
    print_file_info("1.txt")
    append_file("1.txt", "周杰伦")