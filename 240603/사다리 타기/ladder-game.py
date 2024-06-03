n, m = list(map(int, input().split()))
lines = []
for i in range(m):
    lines.append(list(map(int, input().split())))

def find_ladder_answer(lines):
    grid = [[0] * m for _ in range(n)]

    for l in lines:
        r, c = l
        grid[r-1][c-1] = 1
        grid[r][c-1] = -1

    ans = []

    for k in range(n):
        dist = 0
        for i in range(m):
            dist = dist + grid[k+dist][i]
        ans.append(k+dist)
    
    return ans

original_ans = find_ladder_answer(lines)

ans = 6
res = []

def recur(count):
    global res, ans

    if count == m:
        ans = min(ans, len(find_ladder_answer(res)))
        return
    
    res.append(lines[count])
    recur(count + 1)
    res.pop()
    recur(count + 1)

recur(0)

print(ans)