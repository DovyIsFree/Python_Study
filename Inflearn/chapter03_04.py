# chapter03_4
# Python Tuple
# 리스트와 비교 중요
# 튜플 자료형 (순서O, 중복O, 수정X, 삭제X) # 불변

# 선언
a = ()
b = (1,) #데이터가 1개로 선언할 때 ,가 있어야 한다
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', list(e[-1][1])) # 리스트로 형 변환
print()

# 수정x
# d[0] = 1500

# slicing
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])
print()

# Tuple 연산
print('>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print()

# Tuple function
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # return index of 3
print('a - ', a.count(2))
print()

# Packing & Unpacking

# Packing
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

#Unpacking
(x1, x2, x3, x4) = t # 하나로 되어있던 튜플을 풀어서 각각에 넣어줌
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# Packing & Unpacking
t2 = 1, 2, 3 # you can skip ()
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
