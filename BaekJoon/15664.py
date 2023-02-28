# 15664 N과 M (10)

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(combinations(data, m))
answer = list(set(answer))
answer.sort()

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
