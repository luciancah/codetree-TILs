# for i in range(n):
#     arr[i] *= 2
#     sum_diff = 0
#     for j in range(n-1):
#         sum_diff += abs(arr[j+1] - arr[j])

#     max_sum = max(max_sum, sum_diff)
#     arr[i] //=2

n = int(input())
arr = []
arr = list(map(int, input().split()))