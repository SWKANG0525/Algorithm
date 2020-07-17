# Author : Kang Ho Dong
# Date : 2020 - 07 - 16
# Title : BOJ 15649
# Language : Python 3

def func_backtracking(n,m,ls):
    if len(ls) == m and len(ls) != 0:
        for i in ls:
            print(i,end=" ")
        print()
        return

    for i in range(1,n+1):
        temp_var = i
        for j in ls:
            if i == j:
                temp_var = 0

        if temp_var > 0:
            ls.append(temp_var)
            func_backtracking(n,m,ls)
            ls.pop()

N,M = map(int,input().split())
func_backtracking(N,M,[])