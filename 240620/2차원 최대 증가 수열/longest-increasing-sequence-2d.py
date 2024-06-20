n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1

# 초기화
# for i in range(1, n):
#     count = 0
#     for j in range(0, i+1):
#         if grid[0][j] < grid[0][i]:
#             count = max(dp[0][j] + 1, count)
#         dp[0][i] = count


# for i in range(1, n):
#     count = 1
#     for j in range(0, i+1):
#         if grid[j][0] < grid[i][0]:
#             count = max(dp[j][0] + 1, count)
#         dp[i][0] = count

# for i in range(n):
#     print(*dp[i])
# print()

for i in range(1, n):
    for j in range(1, n):
        new_count = 0
        for k in range(0, i+1):
            for l in range(0, j+1):
                if k == i or l == j:
                    continue
                if grid[i][j] > grid[k][l]:
                    new_count = max(new_count, dp[k][l]+1)
        dp[i][j] = new_count

# for i in range(n):
#     print(*dp[i])

ans = 0            
for i in range(n):
    ans = max(ans, max(dp[i]))

print(ans)