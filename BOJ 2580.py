# Author : Kang Ho Dong
# Date : 2020 - 07 - 22
# Title : BOJ 2580
# Language : Python 3
idx = 0
sudoku_board = []
temp_ls = [0] * 81
backtrack_ls = []
def backtrack_sudoku(round):
    global idx
    idx += 1
    print(round)
    if round % 3 == 0 and round != 0:
        sum_1 = sum_2 = sum_3 = 0
        for i in range(round-3,round):
            for j in range(0,9):
                if j<3:
                    sum_1 += sudoku_board[i*9+j]
                elif j<6 and j>=3:
                    sum_2 += sudoku_board[i*9+j]
                elif j<9 and j>=6:
                    sum_3 += sudoku_board[i*9+j]

        if sum_1  == 45 and sum_2  == 45 and sum_3 == 45 and round <9:
            backtrack_sudoku(round+1,backtrack_ls[round+1])
        elif sum_1  == 45 and sum_2  == 45 and sum_3 == 45 and round == 9:
            for i in range(0,9):
                for j in sudoku_board[i*9:i*9+9]:
                    print(j,end=" ")
                print()
                # exit(0)
            return
        else:
            return

    for i in range(round*9,(round+1)*9):
        if sudoku_board[i] == 0:
            for j in range(0,len(ls)):
                sudoku_board[i] = ls[j]
                temp = backtrack_ls.pop(j)
                backtrack_sudoku(round)
                backtrack_ls.insert(j,temp)

    backtrack_sudoku(round+1)


for i in range(0,9):
    sudoku_board += map(int,input().split())

for i in range(0,9):
    t_ls = [0,0,0,0,0,0,0,0,0]
    ls = []
    for j in range(0,9):
        if sudoku_board[i*9+j] != 0:
            t_ls[sudoku_board[i*9+j]-1] = 1

    for j in range(0,9):
        if t_ls[j] == 0:
            ls.append(j+1)
    backtrack_ls.append(ls)

backtrack_sudoku(0)
print(idx)
