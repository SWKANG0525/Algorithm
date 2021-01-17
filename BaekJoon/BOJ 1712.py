# Author : Kang Ho Dong
# Date : 2020 - 06 - 30
# Title : BOJ 1181
# Language : Python 3

input = int(input())

for i in range(1,input*2):
    if i <= input:
        for j in range(0,i):
            print("*",end='')
    else:
        for j in range(0,input*2-i):
            print("*",end='')
    print()