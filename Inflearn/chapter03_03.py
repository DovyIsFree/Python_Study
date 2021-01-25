# chapter03_3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # list inside list
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# indexing
print('>>>>>')
print('d - ',type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# slicing
print('>>>>>')
print('d - ', d[0:3]) # 0 to 2
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# calculate list
print('>>>>>')
print('c + d', c + d) # list + list = list
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0])) #c[0] is int so you should make it to string

# comparing value
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()
# 하나의 주소값을 공유한다 => 하나의 값을 변경하면 다른 하나도 변경 된다

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1:2] = [['a', 'b', 'c']] #리스트 안의 리스트 => 중첩
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] #삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(10)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # index, value
print('a - ', a)
a.reverse()
print('a - ', a)

# del a[9543]
a.remove(10) # delete specific value
print()

print('a - ', a)
print('pop a - ', a.pop()) #LIFO
print('a - ', a)
print('pop a - ', a.pop())
print('a - ', a)
print('4 in a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
