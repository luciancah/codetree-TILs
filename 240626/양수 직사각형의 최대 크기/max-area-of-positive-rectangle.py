n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x0, y0, x1, y1):
    return 0 <= x0 < n and 0 <= x1 <= n and 0 <= y0 < m and 0 <= y1 < m

def is_positive(x0, y0, x1, y1):
    return 0 <= x0 and 0 <= x1 and 0 <= y0 and 0 <= y1

max_area = -1
for x0 in range(n):
    for y0 in range(m):
        area = 0
        for x1 in range(n):
            for y1 in range(m):
                if not in_range(x0, y0, x1, y1):
                    break
                if not is_positive(x0, y0, x1, y1):
                    break
                area += 1
        if area != 0 and area / n == m:
            max_area = max(area, max_area)

print(max_area)