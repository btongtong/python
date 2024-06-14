# 오버라이딩
# 자식 클래스 내에서 부모 클래스와 똑같은 이름의 메소드를 새롭게 정의

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')
        self.make()
        self.send()

b1 = TravelBlackBox('하양이', 300000, 64)
b1.set_travel_mode(10)

b2 = AdvancedTravelBlackBox('초록이', 1200000, 64)
b2.set_travel_mode(15)