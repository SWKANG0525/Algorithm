# Author : Kang Ho Dong
# Date : 2020 - 07 - 26
# Title : BOJ 14888
# Language : Python 3
import operator

max = -1000000001
min = 1000000001
N = int(input())
sequence_ls = list(map(int, input().split()))
operator_ls = list(map(int, input().split()))  # IDX 0 : plus 1 : minus 2 : multiply 3 : divide


def backtrack(sum, n):
    global max, min

    if n == N:

        if sum > max:
            max = sum

        if sum < min:
            min = sum
        return

    for i in range(0, 4):
        if operator_ls[i] != 0:
            if i == 0:
                operator_ls[i] -= 1
                backtrack(sum + sequence_ls[n], n + 1)
                operator_ls[i] += 1
            if i == 1:
                operator_ls[i] -= 1
                backtrack(sum - sequence_ls[n], n + 1)
                operator_ls[i] += 1
            if i == 2:
                operator_ls[i] -= 1
                backtrack(sum * sequence_ls[n], n + 1)
                operator_ls[i] += 1
            if i == 3:
                operator_ls[i] -= 1
                if sum < 0:
                    backtrack(int(sum * -1 // sequence_ls[n]) * -1, n + 1)
                else:
                    backtrack(int(sum // sequence_ls[n]), n + 1)
                operator_ls[i] += 1


backtrack(sequence_ls[0],1)
print(max)
print(min)
