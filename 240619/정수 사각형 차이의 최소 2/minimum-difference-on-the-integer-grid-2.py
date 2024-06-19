import sys

INT_MAX = sys.maxsize

n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
dp = {}

def initialize():
    dp[(0, 0, num[0][0])] = num[0][0]

    for i in range(1, n):
        for k in list(dp.keys()):
            if k[0] == i - 1 and k[1] == 0:
                new_min = min(k[2], num[i][0])
                new_max = max(dp[k], num[i][0])
                if (i, 0, new_min) not in dp:
                    dp[(i, 0, new_min)] = new_max
                else:
                    dp[(i, 0, new_min)] = min(dp[(i, 0, new_min)], new_max)

    for j in range(1, n):
        for k in list(dp.keys()):
            if k[0] == 0 and k[1] == j - 1:
                new_min = min(k[2], num[0][j])
                new_max = max(dp[k], num[0][j])
                if (0, j, new_min) not in dp:
                    dp[(0, j, new_min)] = new_max
                else:
                    dp[(0, j, new_min)] = min(dp[(0, j, new_min)], new_max)

def solve():
    initialize()

    for i in range(1, n):
        for j in range(1, n):
            new_states = {}
            for k in list(dp.keys()):
                if k[0] == i - 1 and k[1] == j:
                    new_min = min(k[2], num[i][j])
                    new_max = max(dp[k], num[i][j])
                    if (i, j, new_min) not in new_states:
                        new_states[(i, j, new_min)] = new_max
                    else:
                        new_states[(i, j, new_min)] = min(new_states[(i, j, new_min)], new_max)
                if k[0] == i and k[1] == j - 1:
                    new_min = min(k[2], num[i][j])
                    new_max = max(dp[k], num[i][j])
                    if (i, j, new_min) not in new_states:
                        new_states[(i, j, new_min)] = new_max
                    else:
                        new_states[(i, j, new_min)] = min(new_states[(i, j, new_min)], new_max)
            dp.update(new_states)

solve()

ans = INT_MAX
for k in range(1, 101):
    if (n - 1, n - 1, k) in dp:
        ans = min(ans, dp[(n - 1, n - 1, k)] - k)

print(ans)