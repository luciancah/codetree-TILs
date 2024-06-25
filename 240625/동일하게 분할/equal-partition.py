n = int(input())
arr = list(map(int, input().split()))
sum_arr = sum(arr)

dp = [0 for _ in range(sum_arr + 1)]
dp[0] = 1

for a in arr:
    dp[a] = 1

for i in range(sum_arr, -1, -1):
    for j in range(n):
        if i - j <= 0:
            continue
        if not dp[i-j]:
            continue
        dp[i] = 1

ans = 'Yes' if dp[sum_arr // 2 + 1] else 'No'


# print(dp)
print(ans)