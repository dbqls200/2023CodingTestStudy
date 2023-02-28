# 19623 회의실 배정 (4)

n = int(input())
time = []
dp = [0] * n

for i in range(n):
    time.append(list(map(int, input().split())))

last = 0

print(time)

if n == 1:
    print(time[0][2])
else:
    dp[0] = time[0][2]
    if time[0][2] >= time[1][2]:
        dp[1] = time[0][2]
        last = time[0][1]
    else:
        dp[1] = time[1][2]
        last = time[1][1]

    for i in range(2, n):
        start, finish, people = time[i]
        if start >= last:
            print(start, finish, people)
            dp[i] = dp[i-1]+time[i][2]
            last = finish
        else:
            dp[i] = dp[i-1]

    print(max(dp))
    print(dp)
