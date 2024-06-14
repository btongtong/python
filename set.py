# 세트
# 세트 = {값1, 값2, 값3, ...}
# 순서 보장 안됨, 중복 허용 안됨

A = {'돈까스', '보쌈', '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}

# 두 친구가 공통으로 좋아하는 음식은?
print(A.intersection(B))

# 두 친구가 좋아하는 음식 모두?
print(A.union(B))

# A만 좋아하는 음식, 공통으로 겹치는 제육덮밥은 너무 자주 먹어서 싫어!
print(A.difference(B))

# 좋아하는 음식 추가
A.add('닭갈비')
print(A)

# 질린 음식 제거
A.remove('제육덮밥')
print(A)

# 다이어트 선언
A.clear()   # 모든 값 삭제
print(A)

del A   # A라는 세트 자체를 없앰
# print(A)