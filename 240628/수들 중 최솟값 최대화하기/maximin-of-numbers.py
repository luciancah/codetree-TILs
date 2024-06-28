n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
grid2 = list(map(list, zip(*grid[::-1])))

# print(grid)
# print(grid2)

ans = 0

def recur(cnt, xidx, yidx, selected, grid):
    # print(cnt, xidx, yidx)
    global ans
    if cnt == n**2:
        return

    if xidx >= n or yidx >= n:
        return
    
    if len(selected) == n:
        ans = max(ans, min(selected))
        return

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx+1, yidx+1, selected, grid)
    selected.pop()
    recur(cnt+1, xidx, yidx, selected, grid)

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx+1, yidx, selected, grid)
    selected.pop()
    recur(cnt+1, xidx, yidx, selected, grid)

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx, yidx+1, selected, grid)
    selected.pop()
    recur(cnt+1, xidx, yidx, selected, grid)

    return

recur(0, 0, 0, [], grid)
a = ans
recur(0, 0, 0, [], grid2)
b = ans

print(max(a, b))