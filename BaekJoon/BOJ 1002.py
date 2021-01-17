# Author : Kang Ho Dong
# Date : 2020 - 07 - 03
# Title : BOJ 1085
# Language : Python 3

import math

T = int(input())

for i in range(0, T):
    xpos1, ypos1, radius1, xpos2, ypos2, radius2 = map(int, input().split())
    distance = math.sqrt((xpos1 - xpos2) * (xpos1 - xpos2) + (ypos1 - ypos2) * (ypos1 - ypos2))

    if distance == 0 and radius1 == radius2:  # Case -1 : Match
        print(-1)
    elif distance == radius2 + radius1:  # Case 1 : Circumscription
        print(1)
    elif distance == abs(radius1-radius2): # Case 1 : inscribe
        print(1)
    elif distance < abs(radius1-radius2):
        print(0)
    elif distance > radius1 + radius2:
        print(0)
    else:
        print(2)