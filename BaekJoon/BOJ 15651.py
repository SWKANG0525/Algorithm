# Author : Kang Ho Dong
# Date : 2020 - 07 - 18
# Title : BOJ 15651
# Language : Python 3

def func_backtracking(n,m,ls):
    if len(ls) == m and len(ls) != 0:
        for i in ls:
            print(i,end=" ")
        print()
        return

    for i in range(1,n+1):
            ls.append(i)
            func_backtracking(n,m,ls)
            ls.pop()

N,M = map(int,input().split())
func_backtracking(N,M,[])