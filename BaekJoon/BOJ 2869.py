# Author : Kang Ho Dong
# Date : 2020 - 07 - 01
# Title : BOJ 2869
# Language : Python 3

import math
up_var,down_var,height = map(int,input().split())

if up_var>=height:
    print(1)
else:
    print(math.ceil((height-up_var)/(up_var-down_var)+1))