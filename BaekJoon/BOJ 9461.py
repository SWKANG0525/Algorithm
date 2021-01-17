# Author : Kang Ho Dong
# Date : 2020 - 08 - 06
# Title : BOJ 9461
# Language : Python 3
sequence_list = [0] * 101
sequence_list[1] = 1
sequence_list[2] = 1
sequence_list[3] = 1


for i in range(4,101):
    sequence_list[i] = sequence_list[i-2]+sequence_list[i-3]

N = int(input())
for i in range(1,N+1):
    test_case = int(input())

    print(sequence_list[test_case])