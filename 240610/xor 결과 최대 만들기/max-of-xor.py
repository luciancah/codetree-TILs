import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
max_ans = 0
ans = 0

def recur(ans, count):
    global max_ans

    if count == m:
        max_ans = max(max_ans, ans)
        return
    
    for num in arr:
        recur(ans^num, count+1)

recur(0, 0)

print(max_ans)