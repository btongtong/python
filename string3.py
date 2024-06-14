# 문자열 출력
python = 'python'
java = 'java'

print(python + ' ' + java)
print(python, java)

print('개발 언어에는 ' + python + ', ' + java + ' 등이 있어요')
print('개발 언어에는', python, ',', java, '등이 있어요')

# 문자열 포맷
print('개발 언어에는 {}, {} 등이 있어요'.format(python, java))
print('개발 언어에는 {1}, {0} 등이 있어요'.format(python, java))
print(f'개발 언어에는 {python}, {java} 등이 있어요')