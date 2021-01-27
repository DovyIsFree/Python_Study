# chapter03_5
# Python Dictionaty
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone' : '01012345678', 'birthday' : '870514'}
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 존재x -> ERROR
print('a - ', a.get('name')) # 존재x -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
