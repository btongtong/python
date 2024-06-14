# init
# 초기화
# 객체가 생성될 때 자동으로 실행된다

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이', 300000)
print(b2.name, b2.price)