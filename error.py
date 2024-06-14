# 에러
# 에러의 원인 파악하기, 서로 다른 에러에 대해 서로 다른 해결을 제시할 수 있게 한다.

try:
    result = 3 / 0
    print(f'연산 결과는 {result}입니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:    # 모든 에러 확인
    print('에러가 발생했어요:', err)