# Author : Kang Ho Dong
# Date : 2020 - 07 - 11
# Title : BOJ 2751
# Language : Python 3
import sys

complete_binary_tree = []
N = int(sys.stdin.readline())

def heapify(idx):

    big_elements = idx * 2 + 1
    if big_elements +1 < N and complete_binary_tree[big_elements] < complete_binary_tree[big_elements+1]:
        big_elements = idx * 2 + 2

    if big_elements < N:
        if complete_binary_tree[idx] < complete_binary_tree[big_elements]:
            complete_binary_tree[idx], complete_binary_tree[big_elements] = complete_binary_tree[big_elements], complete_binary_tree[idx]
        heapify(big_elements)



for i in range (0, N):
    complete_binary_tree.append(int(sys.stdin.readline()))

for i in range(N//2 -1 ,-1,-1):
    heapify(i)

for i in range(N-1,0,-1):
    complete_binary_tree[0],complete_binary_tree[i] = complete_binary_tree[i],complete_binary_tree[0]
    N= N-1
    heapify(0)


for i in complete_binary_tree:
    print(i)
