import sys
input = sys.stdin.readline

values = []
weights = []
n, m = map(int, input().split())
for _ in range(n):
    w, v = map(int, input().split())
    values.append(v)
    weights.append(w)

# dp배열 : 무게 / 금액 / 개수 ?

max_num = m // min(weights) + 1
dp = [[-1 for _ in range(m+1)] for _ in range(max_num)]
for i in range(max_num):
    dp[i][0] = 0

for i in range(max_num):
    for j in range(1, m+1):
        for k in range(i):
            if j >= weights[k]:
                if dp[i][j-weights[k]] == -1:
                    continue
                dp[i][j] = max(dp[i][j], dp[i][j-weights[k]] + values[k])

print(max(dp[-1]))

# for i in range(max_num):
#     print(*dp[i])