from collections import deque

n, m = map(int, input().split())
snake_safe = [[int(x) for x in input().split()] for i in range(n)]
visited = [[0 for col in range(m)] for row in range(n)]

q = deque()
q.append((0, 0, 0))

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

global g_step

while q:
    x, y, step = q.popleft()
    g_step = step
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and snake_safe[ny][nx]:
            visited[ny][nx] = 1
            q.append((nx, ny, step + 1))
if g_step == 0:
    print(-1)
else:
    print(g_step)