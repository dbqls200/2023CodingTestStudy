# 15666 N과 M (12)

from itertools import combinations_with_replacement

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(combinations_with_replacement(data, m))
answer = list(set(answer))
answer.sort()

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
