n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))


'''
원래 접근 : combination 만들어서 걔네 겹치는지 확인 - 최댓값 구하기 (완탐)
nC(1~n) 하면 터지긴 할듯

선분 하나마다 고르고 말고 선택하기 dp배열은 멀로 ? ...
'''

def is_crossed(l1, l2):
    if l1[0] <= l2[0]:
        if l1[1] >= l2[0]:
            return True
    elif l1[0] >= l2[0]:
        if l1[1] <= l2[1]:
            return True
    return False

ans = 0

for k in range(n):
    dp = [1] * n
    dp[k] = 1
    for i in range(k, n):
        max_dp = 1
        for j in range(0, i):
            if not is_crossed(lines[i], lines[j]):
                max_dp = max(max_dp, dp[j] + 1)

        dp[i] = max_dp

    ans = max(max(dp), ans)
    # print(dp)

print(ans)