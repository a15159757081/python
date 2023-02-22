class Phone:
    IMEI = None
    producer = "TICAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")


class MyPhone(Phone):
    producer = "ITHEIMA"  # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")  # 复写子类的成员方法
        # 方式一
        print(Phone.producer)  # 在子类的方法中使用复写父类
        # Phone.call_by_5g(self)  # 这里的方法要加self
        # 方式二
        super().call_by_5g()  # 使用super，超类方法
        print("关闭单核模式确保性能")


phone = MyPhone()
phone.call_by_5g()
print(phone.producer)