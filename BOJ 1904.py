# Author : Kang Ho Dong
# Date : 2020 - 08 - 03
# Title : BOJ 1904
# Language : Python 3


N = int(input())
ls = [0] * 1000001
ls[0] = 1
ls[1] = 1

for i in range(2,1000001):
    ls[i] = (ls[i-1]+ls[i-2]) % 15746

print(ls[N])
