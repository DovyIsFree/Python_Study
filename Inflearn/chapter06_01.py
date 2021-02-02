# Chapter06-01
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# Understanding of diffrence between Class and Instance
# namespace : 객체를 인스턴스화 할 때 저장된 공간
# class variance: 직접 접근 가능
# instance variance: 객체마다 별도 존재

# ex1
class Dog: # object 상속
    # 클래스 속성
    species = "firstdog"

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# information of class
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# namespace
print('dog1',a.__dict__)
print('dog2',b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# ex2
# self의 이해

class SelfTest:
    def func1(): #class method
        print('Func1 called')
    def func2(self): #instance method
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f)
print()


# ex3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수, 모든 인스턴스가 공유
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__) #stock_num을 모두가 공유하지만 굳이 표시는 안한다
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)
