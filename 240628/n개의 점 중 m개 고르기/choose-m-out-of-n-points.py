import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]

def calc_dist(d1, d2):
    return (d1[0]-d2[0]) ** 2 + (d1[1]-d2[1]) ** 2

ans = sys.maxsize
selected = set()

def recur(count):
    global ans
    dist = 0
    if len(selected) == m:
        # print(selected)
        for i in selected:
            for j in selected:
                if i==j:
                    continue
                dist = max(dist, calc_dist(i, j))
        ans = min(ans, dist)
        return
    if count == m:
        return
    
    for i in range(n):
        if dots[i] not in selected:
            selected.add(dots[i])
            recur(count + 1)
            selected.remove(dots[i])
            recur(count + 1)

    return

recur(0)
print(ans)