# 메소드: 클래스 내에 정의된 어떤 동작, *기능*을 하는 코드들의 묶음
# 문자열 메소드: 문자열을 다루기 위한 여러 기능

# 문자열.메소드(...)
letter = 'how are YOU?'
print(letter.lower())       # 소문자 변환
print(letter.upper())       # 대문자 변환
print(letter.capitalize())  # 첫 글자만 대문자
print(letter.title())       # 각 단어들의 첫 글자만 대문자
print(letter.swapcase())    # 대소문자 뒤바꾸기 (대문자 -> 소문자, 소문자 -> 대문자)
print(letter.split())       # 문자열 나누기
print(letter.count('how'))  # ()안의 단어가 몇 번 쓰였는지

s = '손으로 쓰면서 외우는 일본어 문법 30일 완성'
print(s.startswith('손으로'))   # ()안의 단어로 시작하는지 True, False로 반환
print(s.endswith('미완성'))     # ()안의 단어로 끝나는지 True, False로 반환

s = '...손으로 쓰면서 외우는 일본어 문법 30일 완성...'
print(s.strip('.'))         # 앞 뒤로 불필요한 부분 제거

s = '손으로 쓰면서 외우는 일본어 문법 30일 완성'
print(s.replace('쓰면서','보면서'))    # ('앞', '뒤') '앞' 글자를 '뒤' 글자로 변환
print(s.find('외우는'))              # ()안의 글자 위치 찾기           
print(s.center(30, '-'))           # (숫자, '문자') 총 길이 숫자 만큼이 되게 '문자'로 감싸기
