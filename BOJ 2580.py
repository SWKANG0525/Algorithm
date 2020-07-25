# Author : Kang Ho Dong
# Date : 2020 - 07 - 22 ~ 2020 - 07 - 25
# Title : BOJ 2580
# Language : Python 3
sudoku_board = []
temp_ls = [0] * 81
backtrack_ls = []


def backtrack_sudoku(idx):
    flag = True
    if idx == 81:
        for i in range(0, 9):
            for j in sudoku_board[i * 9:i * 9 + 9]:
                print(j, end=" ")
            print()
        exit(0)

    square_x = int(idx % 9 / 3) * 3
    square_y = int(idx / 9 / 3) * 3

    if sudoku_board[idx] == 0:
        for i in backtrack_ls[int(idx / 9)]:
            flag = True

            for j in range(0, 9): # Row
                if sudoku_board[int(idx/9)*9+j] == i:
                    flag = False

            for j in range(0, 9):  # Column
                if sudoku_board[idx % 9 + j * 9] == i:
                    flag = False


            for j in range(0, 3):  # Sub-Square
                for k in range(0, 3):
                    if sudoku_board[(square_y + j) * 9 + square_x + k] == i:
                        flag = False
            if flag == True:
                sudoku_board[idx] = i
                backtrack_sudoku(idx + 1)
                sudoku_board[idx] = 0
    else:
        backtrack_sudoku(idx + 1)


for i in range(0, 9):
    sudoku_board += map(int, input().split())

for i in range(0, 9):
    t_ls = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ls = []
    for j in range(0, 9):
        if sudoku_board[i * 9 + j] != 0:
            t_ls[sudoku_board[i * 9 + j] - 1] = 1

    for j in range(0, 9):
        if t_ls[j] == 0:
            ls.append(j + 1)
    backtrack_ls.append(ls)


backtrack_sudoku(0)
