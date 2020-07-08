# Author : Kang Ho Dong
# Date : 2020 - 07 - 08
# Title : BOJ 1436
# Language : Python 3

N = int(input())
number_list=[]
i = 666
while(len(number_list) <10000):
    str_i = str(i)
    for j in range(len(str_i) - 2):
        if str_i[j] == '6' and str_i[j + 1] == '6' and str_i[j + 2] == '6':
            number_list.append(int(i))
            break
    i += 1

print(sorted(number_list)[N-1])