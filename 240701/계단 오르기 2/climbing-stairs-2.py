'''
2n개 주어졌을 때 순서 유지 n개 골라서 홀수번째 더하고 짝수번째 빼기
i위치에서 j개 골랐을 때 값 (2차원)

- i 위치 고르지 않는 경우 == i-1 위치에서 j개 골랐을 때
- i 위치 고르는 경우 == i-1 위치에서 j-1개 == i위치에서 j개

n층 높이일 때 1계단 / 2계단 올라가기 (1계단은 최대 3회)
i층일 때 1계단 j회 올라 갔을 때 값 동전의 총액
'''

import sys
int_min = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[int_min]  * (4) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
dp[1][0] = 0
dp[1][1] = arr[1]
dp[2][0] = arr[2]

for i in range(2, n+1):
    for j in range(4):
        dp[i][j] = max(dp[i-1][j-1] + arr[i], dp[i-2][j] + arr[i])
    
print(dp[-1][-1])