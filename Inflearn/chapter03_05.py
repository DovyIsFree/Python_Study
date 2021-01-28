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


# 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# check length
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_ites : 반목문(__iter__)에서 사용 가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print()


print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)
print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

print('a - ', 'birth' in a) # in연산자는 key를 포함하고 있는지 check
print('d - ', 'City' in d)
print()

# 수정 & 추가
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)
