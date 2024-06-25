n = int(input())
nums = list(map(int, input().split()))

# dp = a, b 그룹이라고 할 때 a 그룹에 n개 / 값은 두 그룹의 차

dp = [0 for _ in range(n + 1)]
dp[0] = 0
sum_nums = sum(nums)

for i in range(n):
    for j in range(n, -1, -1):
        if j >= i:
            sum_selected = dp[j-i] + nums[i]
            # print(i, j, sum_nums, sum_selected, sum_nums-dp[i])
            dp[j] = dp[i] if abs(abs(sum_nums - dp[j]) - dp[j]) < abs(abs(sum_nums - sum_selected) - sum_selected) else sum_selected

# print(dp)

for i in range(len(dp)):
    dp[i] = abs(abs(sum_nums - dp[i]) - dp[i])

print(min(dp))