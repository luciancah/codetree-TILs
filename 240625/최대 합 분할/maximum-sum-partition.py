def max_equal_sum_partition_v2(n, nums):
    # 총합 계산
    total_sum = sum(nums)

    # dp[i][j][k]: i개의 수를 사용해서 그룹 A의 합이 j, 그룹 B의 합이 k인 경우의 가능성
    dp = [[[False] * (total_sum + 1) for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True  # 아무 수도 사용하지 않고 두 그룹의 합이 0이 되는 경우

    for num in nums:
        for i in range(n, 0, -1):
            for j in range(total_sum - num + 1):
                for k in range(total_sum - num + 1):
                    if dp[i-1][j][k]:  # num을 C 그룹에 포함시키는 경우
                        dp[i][j][k] = True
                    if dp[i-1][j-num][k]:  # num을 A 그룹에 포함시키는 경우
                        dp[i][j][k] = True
                    if dp[i-1][j][k-num]:  # num을 B 그룹에 포함시키는 경우
                        dp[i][j][k] = True

    max_equal_sum = 0
    for j in range(total_sum // 2 + 1):
        for k in range(total_sum // 2 + 1):
            if j == k and any(dp[i][j][k] for i in range(n + 1)):
                max_equal_sum = max(max_equal_sum, j)

    return max_equal_sum

n = int(input())
nums = list(map(int, input().split()))

print(max_equal_sum_partition_v2(n, nums))