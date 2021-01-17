# Author : Kang Ho Dong
# Date : 2019 - 07 - 06
# Title : BOJ 2231
# Link : https://www.acmicpc.net/problem/2108 ( Statistics )
# Language : Python 3

N = int(input())

i = int(N / 10)

for i in range(i, N + 1):

    test_case = i
    for j in str(i):
        test_case += int(j)

    if test_case == N:
        print(i)
        break
    elif i == N:
        print(0)

#