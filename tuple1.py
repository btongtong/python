# 튜플
# 튜플(값1, 값2, 값3, ...)
# 튜플: 한 번 만들면 수정 불가능, 읽기 전용 리스트 정도로 생각하기

my_tuple = ('초코송이', '빼빼로', '초코칩 쿠키', '초코송이')    # 중복 허용
your_tuple = (1, 2.4, True, '과자')                     # 아무 자료형이나 넣을 수 있음

# 인덱스에 해당하는 값 (순서 보장)
print(my_tuple[0])

# 슬라이싱
print(my_tuple[1: 3])

# 튜플에 포함 여부
print('초코송이' in my_tuple)

# 튜플 개수 확인
print(len(my_tuple))


