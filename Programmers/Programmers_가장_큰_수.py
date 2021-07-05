from typing import List, DefaultDict
from collections import defaultdict


def solution(numbers: List[int]) -> str:
    answer: str = ''
    number_table: DefaultDict[int] = defaultdict(int)

    for number in numbers:
        number_table[str(number)] += 1

    sorted_keys: List[str] = list(number_table.keys())
    sorted_keys.sort(key=lambda x: x * 3, reverse=True)

    for key in sorted_keys:
        answer += str(key) * number_table[key]

    if answer[0] == '0':
        return "0"
    else:
        return answer