import sys

n = int(input())
dp = [0] * n
a = list(map(int, input().split()))

# 점화식 : 배열 순회하면서 현재 원소 위치에서 가장 긴 증가 부분 수열 길이 구하기


def init():
    for i in range(n):
        dp[i] = -sys.maxsize

    dp[0] = a[0]

init()

for i in range(1, n):
    count = 0
    for j in range(0, i):
        if dp[j] == -sys.maxsize:
            continue

        # if j + a[j] >= i:
        #     dp[i] = max(dp[i], dp[j] + 1)
        if j < i:
            count += 1
        
    dp[i] = count


ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)