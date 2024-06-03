n, m, c = list(map(int, input().split()))
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

res = []

def recur(count):
    global res, ans

    if count == m:
        print(res)
        return
    
    res.append(lines[count])
    recur(count + 1)
    res.pop()

    

recur(0)