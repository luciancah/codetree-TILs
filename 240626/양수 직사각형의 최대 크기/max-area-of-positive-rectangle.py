# # n, m = map(int, input().split())
# # grid = [list(map(int, input().split())) for _ in range(n)]

# # def in_range(x0, y0, x1, y1):
# #     return 0 <= x0 < n and 0 <= x1 <= n and 0 <= y0 < m and 0 <= y1 < m

# # def is_positive(x0, y0, x1, y1):
# #     for i in range(x0, x1 + 1):
# #         for j in range(y0, y1 + 1):
# #             if grid[i][j] <= 0:
# #                 return False

# #     return True

# # max_ans = -1
# # for x0 in range(n):
# #     for y0 in range(m):
# #         for x1 in range(x0, n):
# #             for y1 in range(y0, m):
# #                 if not in_range(x0, y0, x1, y1):
# #                     break
# #                 if is_positive(x0, y0, x1, y1):
# #                     max_ans = max((x1-x0+1)*(y1-y0+1), max_ans)
    
# # max_ans = max_ans if max_ans >= 0 else -1
# # print(max_ans)

# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# down_max = [[0]*m for _ in range(n)]

# for j in range(m):
#     if grid[n-1][j] > 0:
#         down_max[n-1][j] = 1

from itertools import combinations
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

positive_dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]
        if graph[i-1][j-1] > 0:
            positive_dp[i][j] = positive_dp[i-1][j] + positive_dp[i][j-1] - positive_dp[i-1][j-1] + graph[i-1][j-1]
        else:
            positive_dp[i][j] = positive_dp[i-1][j] + positive_dp[i][j-1] - positive_dp[i-1][j-1]

def is_positive_rectangle(sx,sy,ex,ey):
    positive = positive_dp[ex][ey]-positive_dp[ex][sy-1]-positive_dp[sx-1][ey] + positive_dp[sx][sy]
    s = dp[ex][ey]-dp[ex][sy-1]-dp[sx-1][ey] + dp[sx][sy]
    if s == positive:
        return True
    return False

ans = -1
for ax in range(1,n):
    for ay in range(1,n):
        for bx in range(ax,n+1):
            for by in range(ay,n+1):
                if is_positive_rectangle(ax,ay,bx,by):
                    row = abs(ax-bx) + 1
                    col = abs(ay-by) + 1
                    ans = max(ans, row*col)
print(ans)


# 8만
# 양 누적합 (400)
# 총 누적합 (400)