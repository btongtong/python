# 파일 작업
# open(파일명, 열기 모드(r, w), encoding='인코딩')
f = open('list.txt', 'w', encoding='utf-8')
f.write('김xx\n')
f.write('이xx\n')
f.write('박xx\n')
f.close()

f = open('list.txt', 'r', encoding='utf-8')
# contents = f.read()   # 한번에 가져오기
# print(contents)

for line in f:
    print(line, end='') # 한 줄씩 가져오기. end='': 불필요한 줄 없애기

f.close

