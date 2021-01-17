# Author : Kang Ho Dong
# Date : 2020 - 06 - 30
# Title : BOJ 1181
# Language : Python 3


num = int(input())
space_var = 0

for i in range(num*2):
    if i % 2 != 0:
        print(' ' * space_var, end='')
        print('*' * (num * 2 - i))
        space_var += 1

space_var -= 1

for i in reversed(range(num*2)):
    if i % 2 != 0 and i != num*2-1:
        space_var -= 1
        print(' ' * space_var, end='')
        print('*' * (num * 2 - i))
