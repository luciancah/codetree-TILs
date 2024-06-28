import sys

sys.setrecursionlimit(10000)

n, _ = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]
m = 2

def calc_dist(d1, d2):
    return (d1[0]-d2[0]) ** 2 + (d1[1]-d2[1]) ** 2

ans = sys.maxsize
selected = []

def recur(count):
    global ans
    dist = 0
    if len(selected) == m:
        ans = min(ans, calc_dist(selected[0], selected[1]))
        return
    if count == m:
        return
    
    for i in range(n):
        if dots[i] not in selected:
            selected.append(dots[i])
            recur(count + 1)
            selected.pop()
            recur(count + 1)

    return

recur(0)
print(ans)