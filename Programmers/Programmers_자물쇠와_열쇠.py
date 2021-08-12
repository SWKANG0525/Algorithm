"""
문제 설명

고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.
잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

제한사항
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

입출력 예
key	lock	result
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true

입출력 예에 대한 설명
자물쇠.jpg
key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.
"""

import copy


# 1. Define Rotate Func
def rotate(key):
    N = len(key)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = key[r][c]

    return ret


# 5. Define Check Locked Func
def is_locked(board_part, key, m_idx, n_idx, lock):
    result = []
    for key_m_idx in range(len(key)):
        for key_n_idx in range(len(key)):
            if key[key_m_idx][key_n_idx]:
                board_part[m_idx + key_m_idx][n_idx + key_n_idx] += 1

    for _ in range(len(lock)):
        result.append(board_part[len(key) + _][len(key):len(lock) + len(key)])

    for element in sum(result, []):
        if element != 1:
            return False
    return True


def solution(key, lock) -> bool:
    # 2. Define Board for Exhaustive Search
    board = [[0 for n in range(len(key) * 2 + len(lock))] for m in range(len(key) * 2 + len(lock))]

    # 3. Create Lock Area
    for _ in range(len(lock)):
        board[len(key) + _][len(key):len(key) + len(lock)] = lock[_][:]

    # 4. Exhaustive Search
    for m_idx in range(len(board) - len(key)):
        for n_idx in range(len(board) - len(key)):
            for round_idx in range(4):
                key = rotate(key)
                if is_locked(copy.deepcopy(board), key, m_idx, n_idx, lock):
                    return True

    return False
