'''
dp[0] = 0
dp[1] = 2
dp[2] = 7

dp[3] = (dp[1] + 3) + (dp[2] + 4)

dp[n] = dp[n-2] + 3 + dp[n-1] + 4
'''

n = int(input())
dp = [0] * 1001

dp[0] = 0
dp[1] = 2
dp[2] = 7

for i in range(3, n+1):
    dp[i] = dp[n-2] + 3 + dp[n-1] + 4

print(dp[n] % 1000000007)