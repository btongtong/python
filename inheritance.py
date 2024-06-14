# 상속
# 부모 클래스의 모든 변수와 메소드를 물려받는 것
# class 자손클래스명(부모클래스명):
#   내용

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 300000)

# b1.set_travel_mode(20)
b2.set_travel_mode(10)