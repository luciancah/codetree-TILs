import sys

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

ans = 0
for i in range(n):
    for j in range(1, m):
        if dp[i][j] and (m - j * 2) in arr:
            ans = max(ans, j)

# for i in range(n):
#     print(*dp[i])

print(ans)