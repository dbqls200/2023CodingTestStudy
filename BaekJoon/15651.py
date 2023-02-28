# 15651 N과 M (3)

from itertools import product

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = list(product(arr, repeat=m))
for a in answer:
    for i in a:
        print(i, end=' ')
    print()
