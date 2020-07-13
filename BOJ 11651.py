# Author : Kang Ho Dong
# Date : 2020 - 07 - 14
# Title : BOJ 11651
# Language : Python 3

N = int(input())
ls = [[] for i in range(200001)]

for i in range(0, N):
    xpos, ypos = map(int, input().split())
    if ypos < 0:
        ls[abs(ypos)].append(xpos)
    elif ypos==0:
        ls[0].append(xpos)
    else:
        ls[ypos + 100000].append(xpos)


for i in range(100000,0,-1):
    ls[i].sort()
    for j in ls[i]:
        print(str(j) + " " + str(i * -1))

ls[0].sort()
for j in ls[0]:
    print(str(j) + " " + "0")

for i in range(100001, 200001):
    ls[i].sort()
    for j in ls[i]:
        print(str(j) + " " + str(i - 100000))
