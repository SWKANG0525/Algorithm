# Author : Kang Ho Dong
# Date : 2020 -07 - 14
# Title : BOJ 10814
# Language : Python 3

N = int(input())
ls=[[] for i in range(201)]
for i in range(0,N):
    age, name = map(str,input().split())
    ls[int(age)].append(name)

for i in range(201):
    for j in ls[i]:
        print(str(i)+" "+j)