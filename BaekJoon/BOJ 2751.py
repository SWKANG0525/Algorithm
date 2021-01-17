# Author : Kang Ho Dong
# Date : 2019 - 01 - 25
# Title : BOJ 2751
# Link : https://www.acmicpc.net/problem/2751 ( Merge Sort )
# Language : Python 3
# Algorithm : Divide And Conquer Algorithm.


def merge_sort(ls) : # Recursive Function

    if len(ls) ==1: # If list's elements == 1. ( Divide Finish )
        return ls # Finish Recursive
    else: # Recursive
        mid = int(len(ls) / 2) # ls divide 2.
        L = merge_sort(ls[:mid]) # Divide Half. Left And Right
        R = merge_sort(ls[mid:])
        i,j = 0,0 # idx
        sorted = [] # Finish Merge And Sort list.
        while i < len(L) and j < len(R): # Merge And Sort.
            if L[i] < R[j]:
                sorted.append(L[i])
                i += 1
            else:
                sorted.append(R[j])
                j += 1
        sorted += L[i:] # If L OR R list's elements Remain, Append sorted list.
        sorted += R[j:]
        return sorted # Return list.

before = [] # Not Sorted List.

T = int(input()) # Test_ase

while T != 0:
    T -= 1
    before.append(int(input()))


for i in merge_sort(before): # Print.
    print(i)

