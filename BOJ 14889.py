N = int(input())
sequence_ls = []
start_team_ls = [0] * N
ans_min = 1000000000
for i in range(N):
    sequence_ls.append(list(map(int, input().split())))


def backtrack(n, count):
    global ans_min
    if count == N:
        return
    if n == N / 2:  # 팀을 2개로 나누고 합을 구하고, 차를 구하고 갱신 후 return
        start_sum = 0
        link_sum = 0
        for i in range(0, N):
            for j in range(0, N):
                if start_team_ls[i] == 0:
                    if start_team_ls[j] == 0:
                        link_sum += sequence_ls[i][j]
                elif start_team_ls[i] == 1:
                    if start_team_ls[j] != 0:
                        start_sum += sequence_ls[i][j]

        if link_sum - start_sum < ans_min and link_sum >= start_sum:
            ans_min = link_sum - start_sum
        elif start_sum - link_sum < ans_min and start_sum >= link_sum:
            ans_min = start_sum - link_sum
        return

    start_team_ls[count] = 1
    backtrack(n + 1, count + 1)
    start_team_ls[count] = 0
    backtrack(n , count + 1)


backtrack(0, 0)
print(ans_min)
