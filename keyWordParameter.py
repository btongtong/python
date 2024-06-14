# 키워드
# 함수 파라미터 순서와 상관없이 사용 가능

def order(shot=2, size='Regular', takeout=True):
    print(f'아메리카노 {size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료 되었습니다')

order()
order(2, takeout=True)
order(size='Regular')
order('Regular', takeout=True)  # 키워드를 명시하지 않아서 'Regular'을 shot으로 인식함