import sys

n = int(input())
dp = [0] * n
a = list(map(int, input().split()))

def init():
    for i in range(n):
        dp[i] = -sys.maxsize

    dp[0] = 0

init()

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == -sys.maxsize:
            continue

        if j + a[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)