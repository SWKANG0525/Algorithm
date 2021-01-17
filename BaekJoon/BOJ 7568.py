# Author : Kang Ho Dong
# Date : 2019 - 07 - 06
# Title : BOJ 7568
# Language : Python 3

N = int(input())

ls = []
rank = []
for i in range(N):
    weight, height = map(int, input().split())
    ls.append([weight, height])

for i in range(N):
    count = 1
    for j in range(N):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            count += 1
    rank.append(count)
for i in rank:
    print(i,end=" ")
