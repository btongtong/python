# while
# while 조건:
#   반복 수행 문장

max = 25
weight = 0
item = 3

while weight + item <= max:
    weight += item
    print('add item')
    print(f'총 무게는 {weight} 입니다')