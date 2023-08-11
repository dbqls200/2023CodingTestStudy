# p.178 위에서 아래로

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for a in array:
    print(a, end=' ')
