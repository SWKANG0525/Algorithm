# Author : Kang Ho Dong
# Date : 2020 - 07 - 01
# Title : BOJ 1085
# Language : Python 3

x,y,w,h = map(int,input().split())
case_h = y-0 if y-0 <= h-y else h-y
case_w = x-0 if x-0 <= w-x else w-x

print(case_h if case_h <= case_w else case_w)