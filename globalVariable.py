# 전역 변수
# 함수 밖에서 정의된 변수
# 어디서든 사용 가능

message = '나는야 전역 변수'

print(message)

def no_secret():
    message = '이러면 또 지역변수'
    print(message)

no_secret()
print(message)

def no_secret():
    global message  # 전역변수 사용하겠음. 없으면 여기서 만들겠음을 의미
    message = '이러면 또 전역변수'
    print(message)

no_secret()
print(message)