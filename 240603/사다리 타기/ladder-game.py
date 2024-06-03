n, m = list(map(int, input().split()))
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))

# [1, 0, 1, 0, 0], [-1, 1, -1, 1, 0], [0, -1, 1, -1, 1], [0, 0, -1, 0, -1]

grid = [[0] * m for _ in range(n)]

for l in lines:
    r, c = l
    grid[r-1][c-1] = 1
    grid[r][c-1] = -1
    
ans = []
for k in range(n):
    dist = 0
    for i in range(m):
        dist = dist + grid[k+dist][i]
    ans.append(k+dist)

# [1, 1], [1, 3], [2, 2], [2, 4], [3, 3], [3, 5]