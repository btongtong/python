# 반환값
# 함수 내에서 처리된 결과를 반환
# 1. *여러 개 반환 가능 (콤마로 구분, 튜플)
# 2. 반환되는 즉시 함수 탈출
# def 함수명():
#   수행할 문장
#   return 반환값

def get_price():
    return 15000

# price = 15000
price = get_price();

print(price)

def get_price(is_vip):
    if is_vip:
        return 10000
    else:
        return 15000

customer1 =  True
customer2 = False
price1 = get_price(customer1)
price2 = get_price(customer2)

print(f'customer1 고객님(단골) 비용: {price1}, customer2 고객님(일반) 비용: {price2}')
