# Author : Kang Ho Dong
# Date : 2019 - 02 - 19
# Title : BOJ 1181
# Link : https://www.acmicpc.net/problem/1181 ( Word Sort )
# Language : Python 3

voca_list = []
for i in range(int(input())):
    voca_list.append(input())

voca_list = list(set(voca_list))
sorted = []

for i in voca_list:
    sorted.append((len(i),i))

sorted.sort()

for i,j in sorted:
    print(j)