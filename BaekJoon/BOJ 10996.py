# Author : Kang Ho Dong
# Date : 2020 - 06 - 30
# Title : BOJ 10996
# Language : Python 3

star_amount = int(input())

for i in range(star_amount*2):
    for j in range(star_amount):
        if i % 2 == 0:
            if j%2 == 0:
                print('*',end='')
            else:
                print(' ',end='')
        else:
            if j%2 ==0:
                print(' ',end='')
            else:
                print('*',end='')

    print()
