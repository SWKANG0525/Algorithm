# Author : Kang Ho Dong
# Date : 2020 - 07 - 01
# Title : BOJ 3009
# Language : Python 3


dot1_x, dot1_y = map(int,input().split())
dot2_x, dot2_y = map(int,input().split())
dot3_x, dot3_y = map(int,input().split())

xpos = 0
ypos = 0
if dot1_x != dot2_x and dot1_x != dot3_x:
    xpos = dot1_x
elif dot2_x != dot3_x and dot2_x != dot1_x:
    xpos = dot2_x
else:
    xpos = dot3_x

if dot1_y != dot2_y and dot1_y != dot3_y:
    ypos = dot1_y
elif dot2_y != dot3_y and dot2_y != dot1_y:
    ypos = dot2_y
else:
    ypos = dot3_y

print(str(xpos) + " "+str(ypos))


