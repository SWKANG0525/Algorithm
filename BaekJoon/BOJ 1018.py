N, M = map(int, input().split())

B_ls = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
reverse_ls = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
chess_ls = []
count = 9999

for i in range(0, N):
    ls = list(input())
    chess_ls.append(ls)


def recursive_Chess(inital, x, y, n, count, check_list):
    if n == 8:
        return count

    for i in range(8):
        if chess_ls[y + n][x + i] != check_list[i]:
            count += 1
    if check_list[0] == 'B':
        return recursive_Chess(inital, x, y, n + 1, count, B_ls)
    else:
        return recursive_Chess(inital, x, y, n + 1, count, reverse_ls)


for y in range(N - 7):
    for x in range(M - 7):

        countW = recursive_Chess(chess_ls[y][x], x, y, 0, 0, reverse_ls)
        countB = recursive_Chess(chess_ls[y][x], x, y, 0, 0, B_ls)

        if countW < countB and count > countW:
            count = countW
        elif countB <= countW and count > countB:
            count = countB

print(count)
