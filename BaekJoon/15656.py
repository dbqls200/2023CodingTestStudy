# 15656 N과 M (7)

from itertools import product

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(product(data, repeat=m))
for a in answer:
    for i in a:
        print(i, end=' ')
    print()
