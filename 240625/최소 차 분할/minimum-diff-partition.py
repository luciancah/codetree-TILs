# n = int(input())
# nums = list(map(int, input().split()))

# # dp 배열: a, b 그룹으로 나누었을 때 a 그룹의 합 (index: 고른 개수, value: 합)
# # dp 비교: a그룹, b그룹 차 적은 순

# dp = [-10001 for _ in range(n + 1)]
# dp[0] = 0
# sum_nums = sum(nums)

# for i in range(n):
#     for j in range(n, -1, -1):
#         if j >= i:
#             sum_selected = dp[j-i] + nums[i]
#             # print(i, j, sum_nums, sum_selected, sum_nums-dp[i])
#             dp[j] = dp[j] if abs(abs(sum_nums - dp[j]) - dp[j]) < abs(abs(sum_nums - sum_selected) - sum_selected) else sum_selected

# # print(sum_nums)
# # print(dp)

# for i in range(len(dp)):
#     dp[i] = abs(abs(sum_nums - dp[i]) - dp[i])

# print(min(dp))

n = int(input())
nums = list(map(int, input().split()))

dp = [-10001 for _ in range(n + 1)]
dp[0] = 0
sum_nums = sum(nums)

for i in range(n):
    for j in range(n, -1, -1):
        if j >= i:
            sum_selected = dp[j-i] + nums[i]
            dp[j] = dp[j] if abs(abs(sum_nums - dp[j]) - dp[j]) < abs(abs(sum_nums - sum_selected) - sum_selected) else sum_selected

for i in range(len(dp)):
    dp[i] = abs(abs(sum_nums - dp[i]) - dp[i])

print(min(dp))