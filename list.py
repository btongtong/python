# 리스트
# 리스트 = [값1, 값2, 값3, ...]
my_list = ['초코송이', '초코송이', '초코송이', '다이제', '칸쵸', '초코칩 쿠키']     # 중복 허용
your_list = [1, 2, 3.14, True, False, '아무거나~']                        # 뭐든지 넣을 수 있음
empty_list = []

print(my_list)
print(your_list)
print(empty_list)

# 인덱스에 해당하는 값 (순서 보장)
print(my_list[0])

# 슬라이싱
print(my_list[0:2])

# 리스트에 포함되어 있는지 확인
print('몽쉘' in my_list)

# 리스트안에 몇 개의 값이 있는지 확인
print(len(my_list))

# 리스트 수정
my_list[1] = '몽쉘'
print(my_list)

# 리스트 추가
my_list.append('빼빼로') 
print(my_list)

# 리스트 삭제
my_list.remove('몽쉘')
print(my_list)

# 리스트끼리 더하기
my_list.extend(your_list)
print(my_list)
