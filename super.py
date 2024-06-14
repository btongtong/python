# super
# 부모 클래스를 의미
# 메소드 내에서 super()를 통해 부모 클래스의 메소드에 접근
# BlackBox.메소드(self, ...)
# super().메소드()

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        # BlackBox.__init__(self, name, price)
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')