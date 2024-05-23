n, m = list(map(int, input().split()))
grid = []
bomb = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

for _ in range(n):
    bomb.append(list(map(int, input().split())))

def after_bomb(grid, r, c):
    spr = grid[r][c]-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == r:
                if abs(j - c) <= spr:
                    grid[i][j] = -1

            if j == c:
                if abs(i - r) <= spr:
                    grid[i][j] = -1

def push_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        temp_arr = []
        count = 0
        for j in range(len(grid)):
            if grid[j][i] != -1:
                temp_arr.append(grid[j][i])
                count += 1

        for _ in range(count, len(grid)):
            temp_arr.insert(0, 0)

        new_grid.append(temp_arr)
    return list(map(list, zip(*new_grid)))

def find_bomb_location(grid, col):
    ans = -1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                ans = j

    if ans == -1:
        return [-1, -1]
    else:
        return [col, ans]


for i in range(len(bomb)):
    by, bx = find_bomb_location(grid, bomb[i])
    if bx == -1:
        continue
    else:
        after_bomb(grid, by, bx)
        grid = push_grid(grid)
    
print(grid)