n = int(input())
dp = [0] * 21

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5

for i in range(3, n):
    dp[i] = dp[i-1] * dp[i-2]

print(dp[n])