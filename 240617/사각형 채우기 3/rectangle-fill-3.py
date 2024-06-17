'''
dp[0] = 0
dp[1] = 2
dp[2] = 7
dp[3] = dp[2] * 2 + dp[1] * 3


'''

n = int(input())
dp = [0] * 1001

dp[0] = 0
dp[1] = 2
dp[2] = 7

for i in range(3, n+1):
    dp[i] = dp[i-1] * 2 + dp[i-2] * 4

print(dp[n] % 1000000007)