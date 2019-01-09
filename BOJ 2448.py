# Author Kang Ho Dong
# Date 2019-01-09
# BOJ 2448
# Divide And Conquer Algorithm
import math


stage = []
minunit = ["*","* *","*****"]
# Stage == save lines.
# Minimum Unit =  *
#                * *
#               *****

# Draw minunits until floor == idx

# Recursive Function
# DrawStage Functions Parameter #1 Floor : 3*2^k - 2(math,log(3,2)) , #2 idx : Index line.
def DrawStage(floor, idx):

    if idx == 0:
        for temp in minunit:
            stage.append(temp)

    else:
        #xpos = lines start point
        xpos = 6*(2**(idx-1))-1
        for temp in range(0,len(stage)):
            space = " " * (xpos -2*temp)
            #space = between triangles space
            line =  stage[temp]+ space + stage[temp]
            stage.append(line)

    if round(floor)==idx:
        return

    DrawStage(floor,idx+1)

input_value = int(input())
floor = round(math.log(input_value,2)-math.log(3,2))
DrawStage(floor,0)
# Input Value floor = 3x2^k. 3,6,12,24,48 ..

for temp in range(0,len(stage)):
    print(stage[temp].center(6*(2**floor)-1," "))




