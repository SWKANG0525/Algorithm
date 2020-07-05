# Author : Kang Ho Dong
# Date : 2020 - 07 - 03
# Title : BOJ 2748
# Language : Python 3

N = int(input()) -1
fibo_num = 1
fibo_previous = 1
fibo_pre_previous = 0
for i in range(0,N):
    fibo_num = fibo_previous + fibo_pre_previous
    fibo_pre_previous = fibo_previous
    fibo_previous = fibo_num

if N==-1 :
    print(0)
elif N==1:
    print(1)
else:
    print(fibo_num)