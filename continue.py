# continue

drama = ['시즌1', '시즌2', '시즌3', '시즌4', '시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 건너뛰자')
        continue
    print(f'{x} 시청')