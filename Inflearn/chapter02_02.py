# Chapter02-02
# Python Bagic
# Print Useage

# 기본 선언
n = 700

# out
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = "Change Value" #value and data type are overrided

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력


# ex1)
print(300)
print(int(300))

# ex2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- # NOTE:

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()


# id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 800
n = 800
z = 800
i = 800
# same value -> python makes them in to only one instance


print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8 #변수는 숫자로 시작할 수 없다


# 예약어는 변수명으로 불가능
# ex) for = 3, class = 4 (*ERROR!)
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""
