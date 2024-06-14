# List Comprehension: 새로운 리스트를 간편하게
# 리스트 변수 = [변수 활용 for 변수 in 반복대상 if 조건]

products = ['JOA-2023', 'JOA-2024', 'SIRO-2023', 'SIRO-2024']
recall1 = []

for p in products:
    if p.startswith('SIRO'):
        recall1.append(p)

print(recall1)

my_list = [1, 2, 3, 4, 5]
new_list = [x for x in my_list if x > 3]
# 1. my_list 에서
# 2. 3보다 큰 값들만
# 3. 그대로 사용해서
# 4. 새로운 리스트로 만들어줘

print(new_list)

recall2 = [p for p in products if p.startswith('SIRO')]

print(recall2)