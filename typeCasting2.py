# 튜플(값의 수정 추가 삭제가 되지 않는 자료형) 값 변경하기
# 튜플 -> 리스트, 리스트 값 추가, 리스트 -> 튜플
my_tuple = ('초코송이', '초코칩 쿠키')
my_list = list(my_tuple)
my_list.append('다이제')
my_tuple = tuple(my_list)

print(my_tuple)

# 리스트(중복 허용)의 중복 값 삭제 (순서 중요 x)
# 리스트 -> 세트, 세트 -> 리스트
my_list = ('초코송이', '초코송이', '초코칩 쿠키', '다이제')
my_set = set(my_list)
my_list = list(my_set)

print(my_list)

# 순서 유지가 중요할 때
# 리스트 -> 딕셔너리(key는 중복 허용 안 함), 딕셔너리 -> 리스트
my_list = ('초코송이', '초코송이', '초코칩 쿠키', '다이제')
my_dic = dict.fromkeys(my_list)
my_list = list(my_dic)

print(my_list)