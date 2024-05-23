n, m, k = list(map(int, input().split()))
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

def rotate_cw(arr):
    return list(map(list, zip(*arr[::-1])))

def rotate_ccw(arr):
    return list(map(list, zip(*arr)))[::-1]

def fall_list(arr):
    new_list = []
    for i in range(len(arr)):
        if arr[i] != 0:
            new_list.append(arr[i])
    
    for _ in range(len(arr) - len(new_list)):
        new_list.append(0)

    return new_list

def fall_grid(grid):
    cw_grid = rotate_cw(grid)
    new_grid = []
    for i in range(len(grid)):
        new_grid.append(fall_list(cw_grid[i]))
    
    return rotate_ccw(new_grid)

def check_bomb(arr, m):
    length = len(arr)
    new_arr = []
    i = 0

    while (i < len(arr)):
        j = i
        while (j < len(arr) - 1 and arr[j] == arr[j+1]):
            j += 1
        if (j - i + 1 >= m):
            i = j + 1
        else:
            new_arr.extend(arr[i:j+1])
            i = j + 1

    new_arr.extend([0] * (len(arr) - len(new_arr)))

    return new_arr

def check_bomb_grid(grid, m):
    grid_cw = rotate_cw(grid)
    new_grid = []
    for i in range(len(grid)):
        new_grid.append(check_bomb(grid_cw[i], m))

    return rotate_ccw(new_grid)

def count_bomb(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                count += 1
    return count

c = 0
for i in range(k):
    prev_count = -1
    count = count_bomb(grid)

    while prev_count != count:
        c += 1
        prev_count = count
        grid = check_bomb_grid(grid, m)
        count = count_bomb(grid)

    grid = rotate_cw(grid)
    grid = fall_grid(grid)
    
    prev_count = -1
    while prev_count != count:
        c += 1
        prev_count = count
        grid = check_bomb_grid(grid, m)
        count = count_bomb(grid)

    c += 1

print(c)
print(count_bomb(grid))