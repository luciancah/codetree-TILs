from collections import deque

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(k)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y]:
        return False
    return True

def push(x, y):
    global order

    q.append((x, y))
    visited[x][y] = 1
    answer[x][y] = order
    order += 1

q = deque()
visited = [[0] * n for _ in range(n)]
answer = [[0] * n for _ in range(n)]

dxs, dys = [1, 0, 0, -1], [0, 1, -1, 0]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)