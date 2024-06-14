# 딕셔너리
# 딕셔너리 = {key1:value1, key2:value2, key3:value3, ...}
# key, value 쌍으로 이루어짐, key 는 중복 허용 안함

person = {
    '이름': '이유미',
    '나이': 25,
    '키': 166,
    '몸무게': 62
}

# key에 해당하는 value 찾기
print(person['이름'])
print(person['나이'])

# print(person['별명'])     # 없는 key에 접근하면 Error
print(person.get('별명'))   # 없는 key에 접근하면 None

# 데이터 추가
person['최종학력'] = '전문대학'
print(person.get('최종학력'))

# 특정 key의 value를 바꾸기
person['몸무게'] = 58
print(person['몸무게'])

# 여러 key의 value를 바꾸기
person.update({'키': 106, '몸무게': 16, '별명': 'T미'})
print(person['키'], person['몸무게'], person['별명'])

# 어떤 key 들이 들어 있는지 확인
print(person.keys())

# 어떤 value 들이 들어 있는지 확인
print(person.values())

# 어떤 key, value 들이 들어 있는지 확인
print(person.items())

# 특정 key, value 삭제
person.pop('키')
print(person.get('키'))

# 모든 데이터 삭제
person.clear()
print(person)
