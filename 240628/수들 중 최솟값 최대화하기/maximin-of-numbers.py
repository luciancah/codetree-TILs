n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def recur(cnt, xidx, yidx, selected):
    global ans
    if cnt == n**2:
        return
    
    if len(selected) == n:
        ans = max(ans, min(selected))
        return

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx+1, yidx+1, selected)
    selected.pop()

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx+1, yidx, selected)
    selected.pop()

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx, yidx+1, selected)
    selected.pop()

    selected.append(grid[xidx][yidx])
    recur(cnt+1, xidx, yidx, selected)
    selected.pop()

    return

recur(0, 0, 0, [])
print(ans)