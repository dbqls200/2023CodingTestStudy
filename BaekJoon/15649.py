# 15649 N과 M (1)

from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
answer = list(permutations(arr, m))
for a in answer:
    for i in a:
        print(i, end=' ')
    print()
