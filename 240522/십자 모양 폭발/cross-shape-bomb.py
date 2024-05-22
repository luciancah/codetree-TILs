n = int(input())
grid = []
bomb = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

bomb = list(map(int, input().split()))

# [[1, 2, -1, 3],
# [3, -1, -1, 3],
# [3, 1, 6, 2],
# [4, 5, 4, 4]]

# (1, 3) ???
# (2, 3)

def after_bomb(grid, r, c):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == 1 and j == 3:
                print(abs(j-c), abs(i-r))
            if i == r:
                if abs(j - c) <= (grid[r][c] - 1):
                    print('1', i, j, abs(j-c), grid[r][c]-1)
                    grid[i][j] = -1

            if j == c:
                if abs(i - r) <= grid[r][c] - 1:
                    print('2', i, j)
                    grid[i][j] = -1
    
    print(grid)

def push_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        temp_arr = []
        count = 0
        for j in range(len(grid)):
            # print(grid[j][i])
            if grid[j][i] != -1:
                temp_arr.append(grid[j][i])
                count += 1

        for _ in range(count, len(grid)):
            temp_arr.append(0)

        new_grid.append(temp_arr)

    for i in range(len(grid)):
        for j in range(len(grid)):
            print(new_grid[j][i])


after_bomb(grid, bomb[0]-1, bomb[1]-1)
# push_grid(grid)