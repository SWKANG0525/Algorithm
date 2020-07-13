# Author : Kang Ho Dong
# Date : 2020 - 07 - 14
# Title : BOJ 11650
# Language : Python 3

N = int(input())
ls = [[] for i in range(200001)]

for i in range(0, N):
    xpos, ypos = map(int, input().split())
    if xpos < 0:
        ls[abs(xpos)].append(ypos)
    elif xpos==0:
        ls[0].append(ypos)
    else:
        ls[xpos + 100000].append(ypos)


for i in range(100000,0,-1):
    ls[i].sort()
    for j in ls[i]:
        print(str(i * -1) + " " + str(j))

ls[0].sort()
for j in ls[0]:
    print("0" + " " + str(j))

for i in range(100001, 200001):
    ls[i].sort()
    for j in ls[i]:
        print(str(i - 100000) + " " + str(j))
