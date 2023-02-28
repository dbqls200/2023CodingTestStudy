# 15663 N과 M (9)

from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))

answer = list(permutations(data, m))
answer = list(set(answer))
answer.sort()

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
