# Author : Kang Ho Dong
# Date : 2019 - 02 - 01
# Title : BOJ 2108
# Link : https://www.acmicpc.net/problem/2108 ( Statistics )
# Language : Python 3

from collections import Counter

def findmode(ls): # Caculate mode func
    sorted = []
    cnt = Counter(ls)
    mode = cnt.most_common()
    mode_v = mode[0][1]

    for i in mode:
        if i[1] == mode_v:
            sorted.append(i[0])

    if len(sorted) == 1:
        return sorted[0]
    else:
        return sorted[1]

data = [] # Dataset
test_case = int(input()) # T = Test_case
sum = 0 # Sum of All Elements.
median = int(test_case/2) 

for i in range(0,test_case): # Append Data
    input_data = int(input())
    sum += input_data
    data.append(input_data)

data.sort() 

print(round(sum/test_case))
print(data[median])
print(findmode(data))
print(data[len(data)-1]-data[0])