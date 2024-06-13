from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    global me
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] > me:
        return False
    return True

def push(x, y):
    global order

    answer[x][y] = order
    visited[x][y] = True
    q.append((x, y))
    order += 1


def bfs():
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

r, c = r, c
me = grid[r-1][c-1]
for i in range(k):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    order = 1
    

    push(r-1, c-1)
    bfs()

for i in range(n):
    print(*answer[i])