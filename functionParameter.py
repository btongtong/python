# 전달값
# 1. 여러 개 사용 가능 (콤마로 구분)
# 2. 함수 내에서만 사용 가능
# def 함수명(파라미터):
#   파라미터를 활용하여 실행할 문장

def show_price(customer):
    print(f'{customer} 고객님')
    print('커트 가격은 10000원 입니다.')

customer1 = '이단발'
show_price(customer1)