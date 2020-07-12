# Author : Kang Ho Dong
# Date : 2020 - 07 - 11
# Title : BOJ 2751
# Language : Python 3
import sys

complete_binary_tree = []
N = int(sys.stdin.readline())

def heapify(idx):

    if idx * 2 + 2 < N:
        big_elements = 2 * idx + 1 if complete_binary_tree[2 * idx + 1] > complete_binary_tree[2 * idx + 2] else 2 * idx + 2
        if complete_binary_tree[big_elements] > complete_binary_tree[idx]:
            complete_binary_tree[idx], complete_binary_tree[big_elements] = complete_binary_tree[big_elements], complete_binary_tree[idx]
        heapify(idx*2+1)
        heapify(idx*2+2)
    elif idx*2 + 1 < N:
        big_elements = 2 * idx + 1
        if complete_binary_tree[big_elements] > complete_binary_tree[idx]:
            complete_binary_tree[idx], complete_binary_tree[big_elements] = complete_binary_tree[big_elements], complete_binary_tree[idx]
        heapify(idx*2+1)
    else:
        return

for i in range (0, N):
    complete_binary_tree.append(int(sys.stdin.readline()))

heapify(0)
for i in range(N-1,0,-1):
    heapify(0)
    complete_binary_tree[0],complete_binary_tree[i] = complete_binary_tree[i],complete_binary_tree[0]
    N=N-1

for i in complete_binary_tree:
    print(i)
