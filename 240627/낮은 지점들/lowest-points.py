n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]
# offset = 10**9

dots.sort(key=lambda x:(x[0], x[1]))
ans = []

cache = 1000000001
for i in range(n):
    flag = True
    if dots[i][0] != cache:
        ans.append(dots[i])
        cache = dots[i][0]

ans2 = 0
for i in range(len(ans)):
    ans2 += ans[i][1]

print(ans2)