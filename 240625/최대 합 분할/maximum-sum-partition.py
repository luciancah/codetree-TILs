import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(1, n+1):
    for j in range(m+1):
        if j >= arr[i] and dp[i-1][j-arr[i]]:
            dp[i][j] = True
        if dp[i-1][j]:
            dp[i][j] = True

ans = -sys.maxsize
for i in range(n):
    for j in range(1, m):
        if dp[i][j] and j == m-j:
            ans = max(ans, j)

print(ans)