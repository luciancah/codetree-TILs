import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[{'mx': 0, 'mn': 0} for _ in range(n)] for _ in range(n)]

def init():
    dp[0][0]['mx'] = grid[0][0]
    dp[0][0]['mn'] = grid[0][0]

    for i in range(1, n):
        dp[i][0]['mn'] = min(dp[i-1][0]['mn'], grid[i][0])
        dp[i][0]['mx'] = max(dp[i-1][0]['mx'], grid[i][0])

    for i in range(1, n):
        dp[0][i]['mn'] = min(dp[0][i-1]['mn'], grid[0][i])
        dp[0][i]['mx'] = max(dp[0][i-1]['mx'], grid[0][i])


init()

for i in range(1, n):
    for j in range(1, n):
        # dp[i][j]['mn'] = min(max(dp[i-1][j]['mn'], dp[i][j-1]['mn']), grid[i][j])
        # dp[i][j]['mx'] = max(min(dp[i-1][j]['mx'], dp[i][j-1]['mx']), grid[i][j])

        p1 = abs(min(dp[i-1][j]['mn'], grid[i][j]) - max(dp[i-1][j]['mx'], grid[i][j]))
        p2 = abs(min(dp[i][j-1]['mn'], grid[i][j]) - max(dp[i][j-1]['mx'], grid[i][j]))

        if p1 <= p2:
            dp[i][j]['mn'] = min(dp[i-1][j]['mn'], grid[i][j])
            dp[i][j]['mx'] = max(dp[i-1][j]['mx'], grid[i][j])
        else:
            dp[i][j]['mn'] = min(dp[i][j-1]['mn'], grid[i][j])
            dp[i][j]['mx'] = max(dp[i][j-1]['mx'], grid[i][j])



print(abs(dp[-1][-1]['mx'] - dp[-1][-1]['mn']))