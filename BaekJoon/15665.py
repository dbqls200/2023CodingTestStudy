# 15665 N과 M (11)

from itertools import product

n, m = map(int, input().split())
data = list(map(int, input().split()))

answer = list(product(data, repeat=m))
answer = list(set(answer))
answer.sort()

for a in answer:
    for i in a:
        print(i, end=' ')
    print()
