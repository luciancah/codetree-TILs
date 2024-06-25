n, m = map(int, input().split())
quests = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [100000001 for _ in range(m + 1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(m, -1, -1):
        if j >= i:
            if dp[j-quests[i][0]] == 100000001:
                continue
            dp[j] = min(dp[j], dp[j-quests[i][0]] + quests[i][1])

print(dp)
print(dp[-1])