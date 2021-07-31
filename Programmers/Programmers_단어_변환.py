"""

"""

from typing import List

answer: int = -1


def solution(begin: str, target: str, words: List[str]):
    def recursive_func(translate: str, turn: int, words: List[str]):
        global answer
        if translate == target and (answer == -1 or answer > turn):
            print(turn, translate)
            answer = turn
            return
        for words_idx in range(len(words)):
            count = 0
            for idx in range(len(words[0])):
                if words[words_idx][idx] != translate[idx]:
                    count += 1
            if count == 1:
                recursive_func(words[words_idx], turn + 1, words[:words_idx] + words[words_idx + 1:])

    recursive_func(begin, 0, words)

    if answer == -1:
        return 0
    else:
        return answer
