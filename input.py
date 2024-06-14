# input
# 사용자로부터 입력을 받는다

name = input('예약자분 성함이 어떻게 되나요?')
print(name)

num = input('총 몇 분이세요?')
if int(num) >= 4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다.')