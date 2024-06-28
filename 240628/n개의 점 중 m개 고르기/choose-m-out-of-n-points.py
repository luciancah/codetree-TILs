import sys

n, m = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]

def calc_dist(d1, d2):
    return (d1[0]-d2[0]) ** 2 + (d1[1]-d2[1]) ** 2

ans = sys.maxsize
selected = []

def recur(count):
    global ans
    if count == m:
        print(selected)
        return
    
    for i in range(n):
        selected.append(dots[i])
        recur(count + 1)
        selected.pop()
        recur(count + 1)

recur(0)