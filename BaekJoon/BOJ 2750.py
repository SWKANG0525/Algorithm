N = int(input())
ls = []
for i in range(0,N):
    ls.append(int(input()))

for i in range(0,N):
    for j in range(i+1,N):
        if ls[i] > ls[j]:
            temp = ls[j]
            ls[j] = ls[i]
            ls[i] = temp

for i in ls:
    print(i)


