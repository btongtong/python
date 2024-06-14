# break: 반복수행을 즉시 멈추고 반복문 탈출하는 역할

drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    print(f'{x} 시청')