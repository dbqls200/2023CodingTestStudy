# 1931 회의실 배정

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

last = 0
cnt = 0
print(arr)
arr = sorted(arr, key = lambda x:x[0])
print(arr)
arr = sorted(arr, key = lambda x:x[1])
print(arr)

for start, finish in arr:
    if start >= last:
        cnt += 1
        last = finish

print(cnt)
