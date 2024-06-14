# 지역변수
# 함수 내에서 정의된 변수
# 함수 내에서만 사용 가능

def secret():
    message = '이건 나만의 비밀'
    print(message)
    message = '함수 내에서는 자유롭게 수정 가능'

# 안됨
# print(message)

# def please():
#     print(message)

def please():
    message = '이렇게 하면 되지?'   # 이름만 같을 뿐 같은 변수가 아님
    print(message)