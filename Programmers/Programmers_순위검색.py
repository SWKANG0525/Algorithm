from typing import List
from typing import Dict
from collections import defaultdict
import itertools
import bisect


def solution(info: str, query: str) -> List:
    answer: List = []
    dict_table: Dict = defaultdict(list)
    for _ in info:
        language = ['-']
        jobs = ['-']
        carrer = ['-']
        foods = ['-']

        split_info = _.split(' ')
        score = split_info[-1]
        language.append(split_info[0])
        jobs.append(split_info[1])
        carrer.append(split_info[2])
        foods.append(split_info[3])
        nCr = list(map(''.join, itertools.product(language, jobs, carrer, foods)))

        for element in nCr:
            dict_table[element].insert(bisect.bisect_left(dict_table[element], int(score)), int(score))

    for seq in query:
        seq = ''.join(seq).split(' and')
        seq = ''.join(seq).split(' ')
        seq_list = dict_table[''.join(seq[:-1])]
        seq_len = len(seq_list)

        if seq[-1] != '-':
            seq_len = seq_len - bisect.bisect_left(seq_list, int(seq[-1]))
        answer.append(seq_len)

    return answer