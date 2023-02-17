class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(1000, 3000)  # 音频，时间


clock1 = Clock()
clock1.id = "0012024"
clock1.price = 19.99
print(f"闹钟id{clock1.id},价格{clock1.price}")
clock1.ring()

clock1 = Clock()
clock1.id = "0012025"
clock1.price = 29.99
print(f"闹钟id{clock1.id},价格{clock1.price}")
clock1.ring()