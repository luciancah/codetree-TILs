from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(k)]
starts = [[r-1, c-1] for r, c in starts]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y]:
        return False
    return True

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                q.append((x, y))
                visited[x][y] = 1

def calc_visited(grid):
    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                res += 1

    return res


rocks = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rocks.append([i, j])

max_visited = 0


def create_grid(rocks):
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if [i, j] in rocks:
                new_grid[i][j] = 1
    return new_grid


for nr in combinations(rocks, len(rocks)-m):
    grid = create_grid(list(nr))
    visited = [[0] * n for _ in range(n)]

    for r, c in starts:
        q = deque()
        q.append((r, c))
        visited[r][c] = 1
        bfs()

        max_visited = max(calc_visited(visited), max_visited)

print(max_visited)