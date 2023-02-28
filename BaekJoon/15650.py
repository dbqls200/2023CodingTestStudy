# 15650 N과 M (2)

from itertools import combinations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = list(combinations(arr, m))
for a in answer:
    for i in a:
        print(i, end=' ')
    print()
