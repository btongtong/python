# 가변인자
# 개수가 바뀔 수 있는 인자
# 전달값이 많으면 마지막에 한 번만 사용 가능하다

def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2024년 06월 14일 금', '이장발')
visit('2024년 06월 14일 금', '이장발', '이단발')
visit('2024년 06월 14일 금', '이장발', '이단발', '이파마')