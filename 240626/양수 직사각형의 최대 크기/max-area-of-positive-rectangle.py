n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x0, y0, x1, y1):
    return 0 <= x0 < n and 0 <= x1 <= n and 0 <= y0 < m and 0 <= y1 < m

def is_positive(x0, y0, x1, y1):
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            if grid[i][j] <= 0:
                return False

    return True

max_ans = -1
for x0 in range(n):
    for y0 in range(m):
        for x1 in range(x0, n):
            for y1 in range(y0, m):
                if not in_range(x0, y0, x1, y1):
                    break
                if is_positive(x0, y0, x1, y1):
                    max_ans = max((x1-x0+1)*(y1-y0+1), max_ans)
    
max_ans = max_ans if max_ans >= 0 else -1
print(max_ans)