# p.182 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] >= b[i]:
        break
    else:
        a[i], b[i] = b[i], a[i]

print(sum(a))
