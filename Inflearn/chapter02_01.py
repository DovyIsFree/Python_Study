# Chapter02-1
# Python Bagic
# Print Useage
# Refrence https://www.python-course.eu/python3_formatted_output.php

print('Python Start!')
print('''Python Start!''')
print("""Python Start!""")
print() #줄 바꿈

# separator option
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='.')
print('010','1234','5678', sep='-')
print('python','naver.com',sep='@')
print()

# end option

print('Welcome to', end=' ') #길게 한 번에 볼 때!
print('IT News', end=' ')
print('Web Site')
print()

# file option
import sys

print('Learn Python', file=sys.stdout)
print()

# format useage(d : 3, s : 'python', f ; 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one','two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) # middle layout

print('%.5s' % ('nice'))
print('%5s' % ('pythonstudy'))
print('%.5s' % ('pythonstudy')) #slicing #space is 5
print('{:10.5}'.format('pythonstudy')) #space is 10, print only 5
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}' .format(42))
print()

# %f
print('%f' % (3.1234567890))
print('{:f}'. format(3.1234567890))
print('%1.8f' % (3.1234567890))

print('%06.2f' % (3.1234567890)) #total digit: 6, dicit digit: 2, left are filled with 0
print('{:06.2f}'. format(3.1234567890))
