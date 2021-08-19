from collections import defaultdict


def solution(fruit_weights, k):
    answer = []
    left_pos = 0
    right_pos = k
    max_weight = max(fruit_weights[left_pos:right_pos])
    print(max_weight)
    fruit_dict = defaultdict(int)
    fruit_dict[max_weight] = 1
    answer.append(max_weight)

    while right_pos < len(fruit_weights):
        print(max_weight)
        left_pos += 1
        right_pos += 1
        if max_weight == fruit_weights[left_pos - 1]:
            max_weight = max(fruit_weights[left_pos:right_pos])
        elif max_weight < fruit_weights[right_pos] and fruit_weights[left_pos] < fruit_weights[right_pos]:
            max_weight = fruit_weights[right_pos]
        elif max_weight < fruit_weights[left_pos] and fruit_weights[right_pos] < fruit_weights[left_pos]:
            max_weight = fruit_weights[left_pos]

        if fruit_dict[max_weight] == 0:
            answer.append(max_weight)
            fruit_dict[max_weight] = 1

    return sorted(answer, reverse=True)

if __name__ == '__main__':
    print(solution([30, 40, 10, 20, 30], 3))