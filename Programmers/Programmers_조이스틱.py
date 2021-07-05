from typing import List,DefaultDict
from collections import defaultdict


def solution(name: str) -> int:
    answer: int = 0
    cursor: int = 0
    char_idx: int = 0
    calc_table: DefaultDict[int] = defaultdict(int)
    while 'A' not in name:
        left_idx = cursor
        right_idx = cursor
        for cursor_idx in range(len(name)):
            temp_idx = cursor_idx+ cursor
            if cursor + cursor_idx > len(name):
                temp_idx = cursor+cursor_idx - len(name)
            if name[cursor-cursor_idx] != 'A':
                left_idx = cursor-cursor_idx
            elif name[temp_idx] != 'A':
                right_idx = temp_idx
        char_idx = min(left_idx,right_idx)
        print(char_idx)
        min_direction = ""

        # Case 1 : Left Move & Up Move
        calc_table["LU"] = len(name) - char_idx + cursor + ord(name[char_idx]) - ord('A')
        # Case 2 : Right Move & Up Move
        calc_table["RU"] = char_idx-cursor + ord(name[char_idx]) - ord('A')
        # Case 3 : Left Move & Down Move
        calc_table["LD"] = len(name) - char_idx + cursor + ord('Z') - ord(name[char_idx]) + 1
        # Case 4 :Right Move & Down Move
        calc_table["RD"] = char_idx-cursor + ord('Z') - ord(name[char_idx]) + 1

        for key in calc_table.keys():
            if min_direction == "" or calc_table[min_direction] > calc_table[key]:
                min_direction = key
        print(min_direction+" "+str(calc_table[min_direction]))
        answer += calc_table[min_direction]
        name = list(name)
        name[char_idx] = 'A'
        name = ''.join(name)
        cursor = char_idx



    return answer