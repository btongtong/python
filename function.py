# 함수
# 어떤 동작을 수행하는 코드들의 묶음
# 여러 곳에서 사용되는 코드는 하나의 함수로 만들자
# 함수는 호출을 통해서만 실행한다

# 정의
# def 함수명():
#   수행할 문장

# 호출
# 함수명()

def show_price():
    print('감성 커트 가격은 15000원 입니다')

customer1 = '이단발'
print(f'{customer1} 고객님')
show_price()

customer2 = '이장발'
print(f'{customer1} 고객님')
show_price()




