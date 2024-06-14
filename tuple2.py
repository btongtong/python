# 패킹
my_tuple = ('초코송이', '다이제', '초코칩 쿠키')

# 언패킹
# pie1 = '초코송이'
# pie2 = '다이제'
# pie3 = '초코칩 쿠키'
(pie1, pie2, pie3) = my_tuple

# Asterisk(*)
numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers   # one = 1, two = 2, others = [3,4,5,6,7,8,9,10] 리스트 형태로
