n, r, c = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
x, y = r-1, c-1

visited = [grid[x][y]]

while(True):
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if grid[y][x] < grid[ny][nx]:
            count += 1
            x = nx
            y = ny
            visited.append(grid[y][x])
            break
    if count == 0:
        break

print(*visited)