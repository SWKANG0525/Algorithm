# Author : Kang Ho Dong
# Date : 2020 - 07 - 01
# Title : BOJ 4153
# Language : Python 3

while(True):
    side_1, side_2,side_3 = map(int,input().split())
    if(side_1 ==0 or side_2 == 0 or side_3 == 0):
        break

    ls = [side_1,side_2,side_3]
    ls.sort(reverse=True)
    if(ls[0]*ls[0] == ls[1]*ls[1]+ls[2]*ls[2]):
        print("right")
    else:
        print("wrong")




