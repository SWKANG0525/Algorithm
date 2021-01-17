# Author : Kang Ho Dong
# Date : 2020 - 07 - 18
# Title : BOJ 15650
# Language : Python 3

def func_backtracking(n,m,ls,idx):
    if len(ls) == m and len(ls) != 0:
        for i in ls:
            print(i,end=" ")
        print()
        return

    for i in range(idx,n+1):
        temp_var = i
        for j in ls:
            if i == j:
                temp_var = 0

        if temp_var > 0:
            ls.append(temp_var)
            func_backtracking(n,m,ls,temp_var+1)
            ls.pop()

N,M = map(int,input().split())
func_backtracking(N,M,[],1)