# Author : Kang Ho Dong
# Date : 2019 - 02 - 01
# Title : BOJ 1427
# Link : https://www.acmicpc.net/problem/1427 ( Sort Inside )
# Language : Python 3



num  = input()
cnt = [0] * 10 # count array
for temp_1 in num:
    cnt[int(temp_1)] += 1

for temp_1 in range(9,-1,-1): # Reverse print
    if cnt[temp_1] != 0:
        for temp_2 in range(0,cnt[temp_1]):
            print(temp_1,end='')