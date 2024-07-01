n = int(input())
arr =[[0,0]] +  [list(map(int, input().split())) for _ in range(n*2)]

# dp[i][j] = 빨간색 i개 파란색 j개 뽑았을때 최대의 합, 답: dp[n][n]

dp = [[-1] * (n*2+1) for _ in range(n*2+1)]
dp[0][0] = 0

for i in range(1, n*2+1):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[0][i] = dp[0][i-1] + arr[i][1]

for i in range(1, n*2+1):
    for j in range(1, n*2+1):
        dp[i][j] = max(dp[i-1][j] + arr[i][0], dp[i][j-1] + arr[i][1])

print(dp)

# [[0, 4, 6, 10, 13], [5, 9, 13, 17, 21], [10, 14, 18, 22, 26], [16, 20, 24, 28, 32], [19, 23, 27, 31, 35]]