# Author : Kang Ho Dong
# Date : 2020 - 07 - 19
# Title : BOJ 9663
# Language : Python 3
ans = 0
N = int(input())
# board = [[False] * N for i in range(N)]
board_a, board_b, board_c = [0]*N, [0]*(2*N-1), [0]*(2*N-1)



def chess_board(round):
    global ans
    if round == N:
        # for k in board:
        #     print(k)
        # print()
        ans += 1
        return

    for i in range(0, N):
        # check = True
        if not (board_a[i] or board_b[round + i] or board_c[round - i + N - 1]):

            board_a[i] = board_b[round+i] = board_c[round-i+N-1] = 1
            chess_board(round + 1)
            board_a[i] = board_b[round+i] = board_c[round-i+N-1] = 0

    # if board[j][i] == 1: N^3 Time Complex
            #     check = False
            # for k in range(0, N):
            #     if j + k == round + i and board[j][k] == 1:
            #         check = False
            #     elif j - k + N - 1 == round - i + N - 1 and board[j][k] == 1:
            #         check = False

        # if check:
        #     board[round][i] = 1
        #     chess_board(round + 1)
        #     board[round][i] = 0


chess_board(0)
print(ans)
