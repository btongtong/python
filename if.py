# if
# if 조건1:
#   이 문장
#   if 조건1-1:
#       이이 문장
# elif 조건2:
#   저 문장
# else:
#   그 문장
# 다음 문장

yellow_card = 0
foul = True

if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴.. 조심해야지')
else:
    print('주의')