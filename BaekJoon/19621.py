# 19621 회의실 배정 (2)

n = int(input())
time = []
dp = [0] * n

for i in range(n):
    time.append(list(map(int, input().split())))

if n == 1:
    print(time[0][2])
else:
    dp[0] = time[0][2]
    dp[1] = max(time[0][2], time[1][2])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+time[i][2])

    print(max(dp))
