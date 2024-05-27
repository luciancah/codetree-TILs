n, m, k = list(map(int, input().split()))
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

end_col = 0

for i in range(n):
    flag = True
    for j in range(k-1, k-1+m):
        if grid[i][j] == 1:
            flag = False
            break
        end_col = i
    break

for j in range(k-1, k-1+m):
    grid[end_col][j] = 1

for i in range(n):
    print(*grid[i])