# 예외 처리
# 수행 문장에서 에러가 발생했을 때 프로그램이 멈추지 않고 계속 수행될 수 있도록 에러를 처리한다
# try:
#   수행 문장
# except:
#   에러 발생 시 수행 문장
# else:
#   정상 동작 시 수행 문장
# finally:
#   마지막으로 수행할 문장

try:
    result = 3 / 0
    print(f'연산 결과는 {result}입니다.')
except:
    print('에러가 발생했어요')
else:
    print('정상 작동했어요')
finally:
    print('수행 종료')