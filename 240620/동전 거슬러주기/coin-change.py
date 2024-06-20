import sys

int_min = -sys.maxsize

n, m = map(int, input().split())
dp = [0] * (m+1)
coin = list(map(int, input().split()))

def init():
    for i in range(m+1):
        dp[i] = int_min
    
    dp[0] = 0

init()

for i in range(1, m+1):
    for j in range(1, n):
        if i >= coin[j]:
            if dp[i-coin[j]] == int_min:
                continue
            dp[i] = max(dp[i], dp[i-coin[j]] + 1)

ans = dp[m]

if ans == int_min:
    ans = -1

print(ans)