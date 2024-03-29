# 12852 1로 만들기 (2)

n = int(input())

dp = [i for i in range(n + 1)]
dp[1] = 0
history = [i for i in range(n + 1)]
history[1] = 0


for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    history[i] = i - 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        history[i] = i // 2
        
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        history[i] = i // 3


print(dp[n])
print(n, end =' ')
print(history)
