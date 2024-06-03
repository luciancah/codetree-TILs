from itertools import combinations

n, m, z = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

res = []
res2 = []
ans = 0

def is_possible(res):
    r1, r2 = res
    if r1[0] == r2[0]:
        if r2[1] - r1[1] < m:
            return False
    return True

pop_list = []
for i in range(n):
    for j in range(n-m+1):
        pop_list.append([i,j])

combs = list(combinations(pop_list, 2))
combs2 = []
for c in combs:
    if is_possible(c):
        combs2.append(c)

r1_max = 0
r2_max = 0
for c in combs2:
    r1, r2 = c
    r1_list = list(grid[r1[0]][r1[1]+i] for i in range(m))
    r2_list = list(grid[r2[0]][r2[1]+i] for i in range(m))

    
    for i in range(m, 0, -1):
        r1_list2 = list(combinations(r1_list, i))
        for r in r1_list2:
            if sum(r) <= z:
                r1_max = max(r1_max, sum([x*x for x in r]))

    for i in range(m, 0, -1):
        r2_list2 = list(combinations(r2_list, i))
        for r in r2_list2:
            if sum(r) <= z:
                r2_max = max(r2_max, sum([x*x for x in r]))

print(r1_max+r2_max)