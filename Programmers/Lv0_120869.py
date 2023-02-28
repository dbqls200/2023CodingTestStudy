# 120869 외계어 사전

from itertools import combinations

def solution(spell, dic):
    temp = [''.join(set(d)) for d in dic]
    for t in temp:
        if set(t) == set(spell):
            return 1
    return 2
