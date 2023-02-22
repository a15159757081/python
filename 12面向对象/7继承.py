class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别ID

    def call_by_5g(self):
        print("2022年新功能：5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()  # 继承之后老的东西也可以用
phone.call_by_5g()


# 多继承
class NFCReader:
    nfc_type = "第5代"
    producer = "RY"

    def read_card(self):
        print("NFC读卡")

    def wirte_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"
    print('HM')

    def read_card(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass  # 补全语法，使用pass替代


phone = MyPhone()
phone.call_by_4g()
phone.wirte_card()
phone.read_card()
print(phone.producer)  # 最后输出的厂商名为HM所有同名属性左边优先于右边
