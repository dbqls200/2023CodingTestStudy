# 15654 N과 M (5)

from itertools import permutations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = list(permutations(arr, m))
answer.sort()

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
