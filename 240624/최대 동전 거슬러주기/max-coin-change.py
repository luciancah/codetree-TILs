n, m = map(int, input().split())
coins = list(map(int, input().split()))

# dp배열 -> 금액 / 코인의 개수
dp = [0 for _ in range(m+1)]
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= coins[j]:
            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

if max(dp) == 0:
    print('-1')
else:
    print(dp[-1])