# Author : Kang Ho Dong
# Date : 2020 - 07 - 03
# Title : BOJ 2447
# Language : Python 3

import math

N = int(input())
ls = [["*"] * N for j in range(N)]


def make_blank(n):

    if n <= 2: # Base
        return
    else:
        for count in range(0,N,n):
            for count2 in range(0,N,n):
                for i in range(math.floor(n / 3), n - math.floor(n / 3)):
                    for j in range(math.floor(n / 3), n - math.floor(n / 3)):
                        ls[count+i][count2+j] = ' '


        return make_blank(math.floor(n / 3))


make_blank(N)

for i in ls:
    for j in i:
        print(j, end='')
    print()
