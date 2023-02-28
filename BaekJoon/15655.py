# 15655 N과 M (6)

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(combinations(data, m))

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
