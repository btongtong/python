# with
# 블럭 벗어나면 자동으로 파일 닫음

with open('list.txt', 'w', encoding='utf-8') as f:
    f.write('with 사용')

with open('list.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    print(contents)