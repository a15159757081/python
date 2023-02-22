class Phone:
    __current_voltage = 0.5  # 表示手机运行电压

    def __keep_single_core(self):  # 私有成员无法直接使用，但是可以通过其他的成员使用
        print("让CPU以单核运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话")


phone = Phone()
# phone.__keep_single_core()  # 私有成员方法无法使用
# print(phone.__current_voltage)  # 私有成员变量无法使用
phone.call_by_5g()


class Phone1:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone1 = Phone1()
phone1.call_by_5g()