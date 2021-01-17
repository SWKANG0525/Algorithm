# Author : Kang Ho Dong
# Date : 2020 - 07 - 30
# Title : BOJ 1003
# Language : Python 3

one_ls = [0] * 41
zero_ls = [0] * 41
N = int(input())

def fibonacci(n):

    if n == 41:
        return

    if n==0:
        one_ls[0] = 0
        zero_ls[0] = 1

    elif n==1:
        one_ls[1] = 1
        zero_ls[1] = 0

    else:
        one_ls[n] = one_ls[n-1]+one_ls[n-2]
        zero_ls[n] = zero_ls[n-1]+zero_ls[n-2]

    fibonacci(n+1)

fibonacci(0)


for i in range(N):
    num =int(input())

    if num==0:
        print(1,0)
    else:
        print(zero_ls[num],one_ls[num])
