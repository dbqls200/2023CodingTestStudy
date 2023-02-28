# 15652 N과 M (4)

from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = list(combinations_with_replacement(arr, m))

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
