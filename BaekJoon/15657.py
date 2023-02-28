# 15657 N과 M (8)

from itertools import combinations_with_replacement

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(combinations_with_replacement(data, m))
for a in answer:
    for i in a:
        print(i, end=' ')
    print()
