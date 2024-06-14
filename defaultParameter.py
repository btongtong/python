# 기본값
# 기본적으로 사용되는 값
# def 함수명(전달값=기본값):
#   수행할 문장

def get_price(is_vip=False):
    if is_vip:
        return 10000
    else:
        return 15000
    
price1 = get_price(True)
price2 = get_price()
price3 = get_price()
print(price1, price2, price3)