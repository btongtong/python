# class
# 여러 변수, 함수를 포함할 수 있다
# 설계도, 설명서
# class 클래스명:
#   정의

class BlackBox:
    pass

b1 = BlackBox() # b1 객체 생성 (BlackBox의 인스턴스)
b1.name = '까망이'
print(b1.name)
print(isinstance(b1, BlackBox))