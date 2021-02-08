# Chapter09-01
# 피일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드: w, 추가모드: a, 텍스트 모드: t, 바이너리 모드: b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example...')

# 파일 읽기(Read)
# ex1
# f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
f = open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\it_news.txt', 'r', encoding='UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

# ex2
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# ex3
# read() : 전체 읽기, read(10) : 10Byte
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

# ex4
# readline : 한 줄 씩 읽기

with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# ex5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\it_news.txt', 'r', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end = '')
print()

# 파일 쓰기 (write)
# ex1
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\contents1.txt', 'w') as f:
# with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# ex2
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\contents1.txt', 'at') as f:
    f.write('I love python2\n')

# ex3
# writelines : 리스트 -> 파일
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\contents2.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n', 'Berry\n']
    f.writelines(list)

# ex4
with open('C:\\Users\\82107\\Desktop\\Github\\Python_Study\\Inflearn\\resource\\contents3.txt', 'w') as f:
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
    print('Test Text Write!', file = f)
